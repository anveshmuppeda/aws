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
        # Create Consumer VPC
        self.consumer_vpc = ec2.Vpc(
            self,
            "ConsumerVPC",
            vpc_name=f"{consumer_app_prefix}-vpc",
            ip_addresses=ec2.IpAddresses.cidr("10.10.0.0/16"),
            enable_dns_hostnames=True,
            enable_dns_support=True,
            subnet_configuration=[]
        )
        
        # Create Internet Gateway for Consumer
        self.consumer_igw = ec2.CfnInternetGateway(
            self,
            "ConsumerInternetGateway",
            tags=[{"key": "Name", "value": f"{consumer_app_prefix}-igw"}]
        )
        
        # Attach Internet Gateway to Consumer VPC
        ec2.CfnVPCGatewayAttachment(
            self,
            "ConsumerIGWAttachment",
            vpc_id=self.consumer_vpc.vpc_id,
            internet_gateway_id=self.consumer_igw.ref
        )

        # Get availability zones (first 1)
        azs = self.availability_zones[:1]

        # Create Consumer Public Subnets
        self.consumer_public_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"ConsumerPublicSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.10.{i}.0/24",
                vpc_id=self.consumer_vpc.vpc_id,
                map_public_ip_on_launch=True,
                tags=[{"key": "Name", "value": f"{consumer_app_prefix}-public-subnet-{i+1}"}]
            )
            self.consumer_public_subnets.append(subnet)
        
        # Create Consumer Private Subnets
        self.consumer_private_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"ConsumerPrivateSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.10.{i+10}.0/24",
                vpc_id=self.consumer_vpc.vpc_id,
                map_public_ip_on_launch=False,
                tags=[{"key": "Name", "value": f"{consumer_app_prefix}-private-subnet-{i+1}"}]
            )
            self.consumer_private_subnets.append(subnet)
        
        # Create Consumer Public Route Table
        self.consumer_public_route_table = ec2.CfnRouteTable(
            self,
            "ConsumerPublicRouteTable",
            vpc_id=self.consumer_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{consumer_app_prefix}-public-rt"}]
        )
        
        # Add route to Internet Gateway
        ec2.CfnRoute(
            self,
            "ConsumerPublicRoute",
            route_table_id=self.consumer_public_route_table.ref,
            destination_cidr_block="0.0.0.0/0",
            gateway_id=self.consumer_igw.ref
        )
        
        # Associate consumer public subnets with public route table
        for i, subnet in enumerate(self.consumer_public_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"ConsumerPublicSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,
                route_table_id=self.consumer_public_route_table.ref
            )
        
        # Create Consumer Private Route Table
        self.consumer_private_route_table = ec2.CfnRouteTable(
            self,
            "ConsumerPrivateRouteTable",
            vpc_id=self.consumer_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{consumer_app_prefix}-private-rt"}]
        )
        
        # Associate consumer private subnets with private route table
        for i, subnet in enumerate(self.consumer_private_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"ConsumerPrivateSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,
                route_table_id=self.consumer_private_route_table.ref
            )
        
        ### PROVIDER VPC SETUP ###
        # Create Provider VPC (using different CIDR to avoid overlap)
        self.provider_vpc = ec2.Vpc(
            self,
            "ProviderVPC",
            vpc_name=f"{provider_app_prefix}-vpc",
            ip_addresses=ec2.IpAddresses.cidr("10.20.0.0/16"),
            enable_dns_hostnames=True,
            enable_dns_support=True,
            subnet_configuration=[]
        )
        
        # Create Internet Gateway for Provider
        self.provider_igw = ec2.CfnInternetGateway(
            self,
            "ProviderInternetGateway",
            tags=[{"key": "Name", "value": f"{provider_app_prefix}-igw"}]
        )
        
        # Attach Internet Gateway to Provider VPC
        ec2.CfnVPCGatewayAttachment(
            self,
            "ProviderIGWAttachment",
            vpc_id=self.provider_vpc.vpc_id,
            internet_gateway_id=self.provider_igw.ref
        )

        # Create Provider Public Subnets
        self.provider_public_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"ProviderPublicSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.20.{i}.0/24",
                vpc_id=self.provider_vpc.vpc_id,
                map_public_ip_on_launch=True,
                tags=[{"key": "Name", "value": f"{provider_app_prefix}-public-subnet-{i+1}"}]
            )
            self.provider_public_subnets.append(subnet)
        
        # Create Provider Private Subnets
        self.provider_private_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"ProviderPrivateSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.20.{i+10}.0/24",
                vpc_id=self.provider_vpc.vpc_id,
                map_public_ip_on_launch=False,
                tags=[{"key": "Name", "value": f"{provider_app_prefix}-private-subnet-{i+1}"}]
            )
            self.provider_private_subnets.append(subnet)
        
        # Create Provider Public Route Table
        self.provider_public_route_table = ec2.CfnRouteTable(
            self,
            "ProviderPublicRouteTable",
            vpc_id=self.provider_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{provider_app_prefix}-public-rt"}]
        )
        
        # Add route to Internet Gateway
        ec2.CfnRoute(
            self,
            "ProviderPublicRoute",
            route_table_id=self.provider_public_route_table.ref,
            destination_cidr_block="0.0.0.0/0",
            gateway_id=self.provider_igw.ref
        )
        
        # Associate provider public subnets with public route table
        for i, subnet in enumerate(self.provider_public_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"ProviderPublicSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,
                route_table_id=self.provider_public_route_table.ref
            )
        
        # Create Provider Private Route Table
        self.provider_private_route_table = ec2.CfnRouteTable(
            self,
            "ProviderPrivateRouteTable",
            vpc_id=self.provider_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{provider_app_prefix}-private-rt"}]
        )
        
        # Associate provider private subnets with private route table
        for i, subnet in enumerate(self.provider_private_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"ProviderPrivateSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,
                route_table_id=self.provider_private_route_table.ref
            )

        ### SECURITY GROUPS ###
        
        # Create Security Group for Consumer EC2 instances
        consumer_ec2_sg = ec2.SecurityGroup(
            self,
            "ConsumerEC2SecurityGroup",
            vpc=self.consumer_vpc,
            security_group_name=f"{consumer_app_prefix}-ec2-sg",
            description="Security group for Consumer EC2 instances",
            allow_all_outbound=True
        )
        
        # Allow SSH from anywhere (you may want to restrict this to your IP)
        consumer_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH from anywhere"
        )
        
        # Allow ICMP (ping)
        consumer_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.10.0.0/16"),
            connection=ec2.Port.all_icmp(),
            description="Allow ICMP from Consumer VPC"
        )
        
        # Create Security Group for Provider EC2 instances
        provider_ec2_sg = ec2.SecurityGroup(
            self,
            "ProviderEC2SecurityGroup",
            vpc=self.provider_vpc,
            security_group_name=f"{provider_app_prefix}-ec2-sg",
            description="Security group for Provider EC2 instances",
            allow_all_outbound=True
        )
        
        # Allow SSH from anywhere (you may want to restrict this to your IP)
        provider_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH from anywhere"
        )
        
        # Allow ICMP (ping)
        provider_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.20.0.0/16"),
            connection=ec2.Port.all_icmp(),
            description="Allow ICMP from Provider VPC"
        )
        
        # Create Security Group for VPC Endpoints
        vpc_endpoint_sg = ec2.SecurityGroup(
            self,
            "ECREndpointSecurityGroup",
            vpc=self.provider_vpc,
            security_group_name=f"{provider_app_prefix}-ecr-endpoint-sg",
            description="Security group for ECR VPC Endpoints",
            allow_all_outbound=False
        )

        # Add ingress rule to VPC Endpoint SG from Provider VPC CIDR
        vpc_endpoint_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.20.0.0/16"),
            connection=ec2.Port.tcp(443),
            description="Allow HTTPS from Provider VPC"
        )

        ### EC2 INSTANCES ###
        
        # Get the latest Amazon Linux 2023 AMI
        amzn_linux = ec2.MachineImage.latest_amazon_linux2023(
            edition=ec2.AmazonLinuxEdition.STANDARD,
            cpu_type=ec2.AmazonLinuxCpuType.X86_64
        )
        
        # Create EC2 instances in Consumer Public Subnets
        for i, subnet in enumerate(self.consumer_public_subnets):
            ec2.CfnInstance(
                self,
                f"ConsumerPublicEC2Instance{i+1}",
                instance_type="t2.micro",
                image_id=amzn_linux.get_image(self).image_id,
                key_name="demo",  # Make sure this key pair exists in your AWS account
                subnet_id=subnet.ref,
                security_group_ids=[consumer_ec2_sg.security_group_id],
                tags=[{"key": "Name", "value": f"{consumer_app_prefix}-public-instance-{i+1}"}]
            )
        
        # Create EC2 instances in Consumer Private Subnets
        for i, subnet in enumerate(self.consumer_private_subnets):
            ec2.CfnInstance(
                self,
                f"ConsumerPrivateEC2Instance{i+1}",
                instance_type="t2.micro",
                image_id=amzn_linux.get_image(self).image_id,
                key_name="demo",  # Make sure this key pair exists in your AWS account
                subnet_id=subnet.ref,
                security_group_ids=[consumer_ec2_sg.security_group_id],
                tags=[{"key": "Name", "value": f"{consumer_app_prefix}-private-instance-{i+1}"}]
            )
        
        # Create EC2 instances in Provider Public Subnets
        for i, subnet in enumerate(self.provider_public_subnets):
            ec2.CfnInstance(
                self,
                f"ProviderPublicEC2Instance{i+1}",
                instance_type="t2.micro",
                image_id=amzn_linux.get_image(self).image_id,
                key_name="demo",  # Make sure this key pair exists in your AWS account
                subnet_id=subnet.ref,
                security_group_ids=[provider_ec2_sg.security_group_id],
                tags=[{"key": "Name", "value": f"{provider_app_prefix}-public-instance-{i+1}"}]
            )
        
        # Create EC2 instances in Provider Private Subnets
        for i, subnet in enumerate(self.provider_private_subnets):
            ec2.CfnInstance(
                self,
                f"ProviderPrivateEC2Instance{i+1}",
                instance_type="t2.micro",
                image_id=amzn_linux.get_image(self).image_id,
                key_name="demo",  # Make sure this key pair exists in your AWS account
                subnet_id=subnet.ref,
                security_group_ids=[provider_ec2_sg.security_group_id],
                tags=[{"key": "Name", "value": f"{provider_app_prefix}-private-instance-{i+1}"}]
            )