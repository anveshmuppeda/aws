from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_lambda as _lambda
)


class VpcEndpointServiceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        consumer_app_prefix = "consumer-app-demo"
        provider_app_prefix = "provider-app-demo"

        ### CONSUMER VPC SETUP ###
        # Create Demo VPC
        self.consumer_vpc = ec2.Vpc(
            self,
            "VPC",
            vpc_name=f"{consumer_app_prefix}-vpc",
            ip_addresses=ec2.IpAddresses.cidr("10.10.0.0/16"),
            enable_dns_hostnames=True,
            enable_dns_support=True,
            # Create VPC without subnets
            subnet_configuration=[]
        )
        
        # Create Internet Gateway
        self.consumer_igw = ec2.CfnInternetGateway(
            self,
            "InternetGateway",
            tags=[{"key": "Name", "value": f"{consumer_app_prefix}-igw"}]
        )
        
        # Attach Internet Gateway to VPC
        ec2.CfnVPCGatewayAttachment(
            self,
            "IGWAttachment",
            vpc_id=self.consumer_vpc.vpc_id,
            internet_gateway_id=self.consumer_igw.ref  # Fixed: Use .ref instead of .attr_internet_gateway_id
        )

        # Get availability zones (first 1)
        azs = self.availability_zones[:1]

        # Create Public Subnets
        self.consumer_provider_public_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"PublicSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.10.{i}.0/24",
                vpc_id=self.consumer_vpc.vpc_id,
                map_public_ip_on_launch=True,
                tags=[{"key": "Name", "value": f"{consumer_app_prefix}-public-subnet-{i+1}"}]
            )
            self.consumer_provider_public_subnets.append(subnet)
        
        # Create Private Subnets
        self.consumer_provider_private_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"PrivateSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.10.{i+10}.0/24",  # 10.10.10.0/24, 10.10.11.0/24
                vpc_id=self.consumer_vpc.vpc_id,
                map_public_ip_on_launch=False,
                tags=[{"key": "Name", "value": f"{consumer_app_prefix}-private-subnet-{i+1}"}]
            )
            self.consumer_provider_private_subnets.append(subnet)
        
        # Create Route Tables
        # Public Route Table
        self.consumer_public_route_table = ec2.CfnRouteTable(
            self,
            "PublicRouteTable",
            vpc_id=self.consumer_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{consumer_app_prefix}-public-rt"}]
        )
        # Add route to Internet Gateway
        ec2.CfnRoute(
            self,
            "PublicRoute",
            route_table_id=self.consumer_public_route_table.ref,  # Fixed: Use .ref instead of .attr_route_table_id
            destination_cidr_block="0.0.0.0/0",
            gateway_id=self.consumer_igw.ref  # Fixed: Use .ref instead of .attr_internet_gateway_id
        )
        # Associate public subnets with public route table
        for i, subnet in enumerate(self.consumer_provider_public_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"PublicSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,  # Fixed: Use .ref instead of .attr_subnet_id
                route_table_id=self.consumer_public_route_table.ref  # Fixed: Use .ref instead of .attr_route_table_id
            )
        
        # Private Route Table
        self.consumer_private_route_table = ec2.CfnRouteTable(
            self,
            "PrivateRouteTable",
            vpc_id=self.consumer_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{consumer_app_prefix}-private-rt"}]
        )
        
        # Associate private subnets with private route table
        for i, subnet in enumerate(self.consumer_provider_private_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"PrivateSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,  # Fixed: Use .ref instead of .attr_subnet_id
                route_table_id=self.consumer_private_route_table.ref  # Fixed: Use .ref instead of .attr_route_table_id
            )
        
        ### Provider VPC SETUP ###
        # Create VPC
        self.provider_vpc = ec2.Vpc(
            self,
            "VPC",
            vpc_name=f"{provider_app_prefix}-vpc",
            ip_addresses=ec2.IpAddresses.cidr("10.10.0.0/16"),
            enable_dns_hostnames=True,
            enable_dns_support=True,
            # Create VPC without subnets
            subnet_configuration=[]
        )
        
        # Create Internet Gateway
        self.provider_igw = ec2.CfnInternetGateway(
            self,
            "InternetGateway",
            tags=[{"key": "Name", "value": f"{provider_app_prefix}-igw"}]
        )
        
        # Attach Internet Gateway to VPC
        ec2.CfnVPCGatewayAttachment(
            self,
            "IGWAttachment",
            vpc_id=self.provider_vpc.vpc_id,
            internet_gateway_id=self.provider_igw.ref  # Fixed: Use .ref instead of .attr_internet_gateway_id
        )

        # Get availability zones (first 1)
        azs = self.availability_zones[:1]

        # Create Public Subnets
        self.provider_public_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"PublicSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.10.{i}.0/24",
                vpc_id=self.provider_vpc.vpc_id,
                map_public_ip_on_launch=True,
                tags=[{"key": "Name", "value": f"{provider_app_prefix}-public-subnet-{i+1}"}]
            )
            self.provider_public_subnets.append(subnet)
        
        # Create Private Subnets
        self.provider_private_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"PrivateSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.10.{i+10}.0/24",  # 10.10.10.0/24, 10.10.11.0/24
                vpc_id=self.provider_vpc.vpc_id,
                map_public_ip_on_launch=False,
                tags=[{"key": "Name", "value": f"{provider_app_prefix}-private-subnet-{i+1}"}]
            )
            self.provider_private_subnets.append(subnet)
        
        # Create Route Tables
        # Public Route Table
        self.provider_public_route_table = ec2.CfnRouteTable(
            self,
            "PublicRouteTable",
            vpc_id=self.provider_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{provider_app_prefix}-public-rt"}]
        )
        # Add route to Internet Gateway
        ec2.CfnRoute(
            self,
            "PublicRoute",
            route_table_id=self.provider_public_route_table.ref,  # Fixed: Use .ref instead of .attr_route_table_id
            destination_cidr_block="0.0.0.0/0",
            gateway_id=self.provider_igw.ref  # Fixed: Use .ref instead of .attr_internet_gateway_id
        )
        # Associate public subnets with public route table
        for i, subnet in enumerate(self.provider_public_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"PublicSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,  # Fixed: Use .ref instead of .attr_subnet_id
                route_table_id=self.provider_public_route_table.ref  # Fixed: Use .ref instead of .attr_route_table_id
            )
        
        # Private Route Table
        self.provider_private_route_table = ec2.CfnRouteTable(
            self,
            "PrivateRouteTable",
            vpc_id=self.provider_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{provider_app_prefix}-private-rt"}]
        )
        
        # Associate private subnets with private route table
        for i, subnet in enumerate(self.provider_private_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"PrivateSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,  # Fixed: Use .ref instead of .attr_subnet_id
                route_table_id=self.provider_private_route_table.ref  # Fixed: Use .ref instead of .attr_route_table_id
            )

        # Create Security Group for ECR VPC Endpoints
        vpc_endpoint_sg = ec2.SecurityGroup(
            self,
            "ECREndpointSecurityGroup",
            vpc=self.provider_vpc,
            security_group_name=f"{provider_app_prefix}-ecr-endpoint-sg",
            description="Security group for ECR VPC Endpoints",
            allow_all_outbound=False  # Endpoints don't need outbound
        )

        # Add ingress rule to ECR Endpoint SG from Lambda SG on all ports over VPC CIDR
        vpc_endpoint_sg.add_ingress_rule(
            peer=lambda_sg,
            connection=ec2.Port.all_traffic(),
            description="Allow all traffic from VPC CIDR (from Lambda)"
        )