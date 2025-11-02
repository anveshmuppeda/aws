from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_lambda as _lambda,
)


class VpcEndpointsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        app_prefix = "vpc-endpoints-demo"

        # Create Demo VPC
        self.demo_vpc = ec2.Vpc(
            self,
            "VPC",
            vpc_name=f"{app_prefix}-vpc",
            ip_addresses=ec2.IpAddresses.cidr("10.10.0.0/16"),
            enable_dns_hostnames=True,
            enable_dns_support=True,
            # Create VPC without subnets
            subnet_configuration=[]
        )
        
        # Create Internet Gateway
        self.igw = ec2.CfnInternetGateway(
            self,
            "InternetGateway",
            tags=[{"key": "Name", "value": f"{app_prefix}-igw"}]
        )
        
        # Attach Internet Gateway to VPC
        ec2.CfnVPCGatewayAttachment(
            self,
            "IGWAttachment",
            vpc_id=self.demo_vpc.vpc_id,
            internet_gateway_id=self.igw.ref  # Fixed: Use .ref instead of .attr_internet_gateway_id
        )

        # Get availability zones (first 1)
        azs = self.availability_zones[:1]

        # Create Public Subnets
        self.public_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"PublicSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.10.{i}.0/24",
                vpc_id=self.demo_vpc.vpc_id,
                map_public_ip_on_launch=True,
                tags=[{"key": "Name", "value": f"{app_prefix}-public-subnet-{i+1}"}]
            )
            self.public_subnets.append(subnet)
        
        # Create Private Subnets
        self.private_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"PrivateSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.10.{i+10}.0/24",  # 10.10.10.0/24, 10.10.11.0/24
                vpc_id=self.demo_vpc.vpc_id,
                map_public_ip_on_launch=False,
                tags=[{"key": "Name", "value": f"{app_prefix}-private-subnet-{i+1}"}]
            )
            self.private_subnets.append(subnet)

        # Create EIP for NAT Gateway first
        # self.nat_eip = ec2.CfnEIP(
        #     self,
        #     "NATGatewayEIP",
        #     domain="vpc",
        #     tags=[{"key": "Name", "value": f"{app_prefix}-nat-eip"}]
        # )
        
        # Create NAT Gateway (in first public subnet)
        # self.nat_gateway = ec2.CfnNatGateway(
        #     self,
        #     "NATGateway",
        #     subnet_id=self.public_subnets[0].ref,  # Fixed: Use .ref instead of .attr_subnet_id
        #     allocation_id=self.nat_eip.attr_allocation_id,
        #     tags=[{"key": "Name", "value": f"{app_prefix}-nat-gateway"}]
        # )
        
        # Create Route Tables
        # Public Route Table
        self.public_route_table = ec2.CfnRouteTable(
            self,
            "PublicRouteTable",
            vpc_id=self.demo_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{app_prefix}-public-rt"}]
        )
        # Add route to Internet Gateway
        ec2.CfnRoute(
            self,
            "PublicRoute",
            route_table_id=self.public_route_table.ref,  # Fixed: Use .ref instead of .attr_route_table_id
            destination_cidr_block="0.0.0.0/0",
            gateway_id=self.igw.ref  # Fixed: Use .ref instead of .attr_internet_gateway_id
        )
        # Associate public subnets with public route table
        for i, subnet in enumerate(self.public_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"PublicSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,  # Fixed: Use .ref instead of .attr_subnet_id
                route_table_id=self.public_route_table.ref  # Fixed: Use .ref instead of .attr_route_table_id
            )
        
        # Private Route Table
        self.private_route_table = ec2.CfnRouteTable(
            self,
            "PrivateRouteTable",
            vpc_id=self.demo_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{app_prefix}-private-rt"}]
        )
        
        # Add route to NAT Gateway
        # ec2.CfnRoute(
        #     self,
        #     "PrivateRoute",
        #     route_table_id=self.private_route_table.ref,  # Fixed: Use .ref instead of .attr_route_table_id
        #     destination_cidr_block="0.0.0.0/0",
        #     nat_gateway_id=self.nat_gateway.ref  # Fixed: Use .ref instead of .attr_nat_gateway_id
        # )
        
        # Associate private subnets with private route table
        for i, subnet in enumerate(self.private_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"PrivateSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,  # Fixed: Use .ref instead of .attr_subnet_id
                route_table_id=self.private_route_table.ref  # Fixed: Use .ref instead of .attr_route_table_id
            )

        # Create Lambda Function Role
        lambda_role = iam.Role(
            self,
            "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonVPCFullAccess"),
            ]
        )

        lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "ecr:DescribeRepositories",
                    "ecr:ListImages"
                ],
                resources=["*"]
            )
        )

        # Create Security Group for Lambda
        lambda_sg = ec2.SecurityGroup(
            self,
            "LambdaSecurityGroup",
            vpc=self.demo_vpc,
            security_group_name=f"{app_prefix}-lambda-sg",
            description="Security group for Lambda function",
            allow_all_outbound=True  # Lambda needs to make outbound calls
        )

        # Create Security Group for ECR VPC Endpoints
        vpc_endpoint_sg = ec2.SecurityGroup(
            self,
            "ECREndpointSecurityGroup",
            vpc=self.demo_vpc,
            security_group_name=f"{app_prefix}-ecr-endpoint-sg",
            description="Security group for ECR VPC Endpoints",
            allow_all_outbound=False  # Endpoints don't need outbound
        )

        # Add outbound rule from Lambda SG to ECR Endpoint SG on all ports over VPC CIDR
        lambda_sg.add_egress_rule(
            peer=vpc_endpoint_sg,
            connection=ec2.Port.all_traffic(),
            description="Allow all traffic to VPC CIDR (for ECR endpoint)"
        )

        # Add ingress rule to ECR Endpoint SG from Lambda SG on all ports over VPC CIDR
        vpc_endpoint_sg.add_ingress_rule(
            peer=lambda_sg,
            connection=ec2.Port.all_traffic(),
            description="Allow all traffic from VPC CIDR (from Lambda)"
        )

        # Base lambda function for s3 testing
        s3_lambda = _lambda.Function(
            self,
            "S3Function",
            function_name=f"{app_prefix}-s3-lambda-function",
            runtime=_lambda.Runtime.PYTHON_3_13,
            code=_lambda.Code.from_asset("lambda/s3"),
            handler="index.lambda_handler",
            role=lambda_role,
            timeout=Duration.seconds(10),
            vpc=self.demo_vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnets=[
                    ec2.Subnet.from_subnet_id(self, f"PrivateSubnetRef{i+1}", subnet.ref)
                    for i, subnet in enumerate(self.private_subnets)
                ]
            ),
            security_groups=[lambda_sg]
        )

        # Base lambda function for ecr testing
        ecr_lambda = _lambda.Function(
            self,
            "ECRFunction",
            function_name=f"{app_prefix}-ecr-lambda-function",
            runtime=_lambda.Runtime.PYTHON_3_13,
            code=_lambda.Code.from_asset("lambda/ecr"),
            handler="index.lambda_handler",
            role=lambda_role,
            timeout=Duration.seconds(10),
            vpc=self.demo_vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnets=[
                    ec2.Subnet.from_subnet_id(self, f"PrivateSubnetRefECR{i+1}", subnet.ref)
                    for i, subnet in enumerate(self.private_subnets)
                ]
            ),
            security_groups=[lambda_sg]
        )

        # Create S3 Gateway Endpoint
        self.s3_gateway_endpoint = ec2.CfnVPCEndpoint(
            self,
            "S3GatewayEndpoint",
            vpc_id=self.demo_vpc.vpc_id,
            service_name=f"com.amazonaws.{self.region}.s3",
            vpc_endpoint_type="Gateway",
            route_table_ids=[self.private_route_table.ref],
        )

        # Create ECR API VPC Endpoint (Interface)
        ecr_api_endpoint = ec2.InterfaceVpcEndpoint(
            self,
            "ECRAPIEndpoint",
            vpc=self.demo_vpc,
            service=ec2.InterfaceVpcEndpointAwsService.ECR,
            subnets=ec2.SubnetSelection(
                subnets=[
                    ec2.Subnet.from_subnet_id(self, f"PrivateSubnetRefECRAPI{i+1}", subnet.ref)
                    for i, subnet in enumerate(self.private_subnets)
                ]
            ),
            security_groups=[vpc_endpoint_sg],
            private_dns_enabled=True
        )

        # Create ECR Docker VPC Endpoint (Interface)
        ecr_dkr_endpoint = ec2.InterfaceVpcEndpoint(
            self,
            "ECRDockerEndpoint",
            vpc=self.demo_vpc,
            service=ec2.InterfaceVpcEndpointAwsService.ECR_DOCKER,
            subnets=ec2.SubnetSelection(
                subnets=[
                    ec2.Subnet.from_subnet_id(self, f"PrivateSubnetRefECRDkr{i+1}", subnet.ref)
                    for i, subnet in enumerate(self.private_subnets)
                ]
            ),
            security_groups=[vpc_endpoint_sg],
            private_dns_enabled=True
        )
