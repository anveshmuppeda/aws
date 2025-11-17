from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    Fn,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_lambda as _lambda,
    aws_elasticloadbalancingv2 as elbv2
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
        
        consumer_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH from anywhere"
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
        
        provider_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH from anywhere"
        )
        
        provider_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.20.0.0/16"),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP from Provider VPC"
        )

        ### EC2 INSTANCES ###
        
        amzn_linux = ec2.MachineImage.latest_amazon_linux2023(
            edition=ec2.AmazonLinuxEdition.STANDARD,
            cpu_type=ec2.AmazonLinuxCpuType.X86_64
        )
        
        # Consumer instances (one public, one private)
        ec2.CfnInstance(
            self,
            "ConsumerPublicInstance",
            instance_type="t2.micro",
            image_id=amzn_linux.get_image(self).image_id,
            key_name="demo",
            subnet_id=self.consumer_public_subnets[0].ref,
            security_group_ids=[consumer_ec2_sg.security_group_id],
            tags=[{"key": "Name", "value": f"{consumer_app_prefix}-public-instance"}]
        )
        
        ec2.CfnInstance(
            self,
            "ConsumerPrivateInstance",
            instance_type="t2.micro",
            image_id=amzn_linux.get_image(self).image_id,
            key_name="demo",
            subnet_id=self.consumer_private_subnets[0].ref,
            security_group_ids=[consumer_ec2_sg.security_group_id],
            tags=[{"key": "Name", "value": f"{consumer_app_prefix}-private-instance"}]
        )
        
        # Provider instances (one public, one private with web server)
        ec2.CfnInstance(
            self,
            "ProviderPublicInstance",
            instance_type="t2.micro",
            image_id=amzn_linux.get_image(self).image_id,
            key_name="demo",
            subnet_id=self.provider_public_subnets[0].ref,
            security_group_ids=[provider_ec2_sg.security_group_id],
            tags=[{"key": "Name", "value": f"{provider_app_prefix}-public-instance"}]
        )
        
        provider_private_instance = ec2.CfnInstance(
            self,
            "ProviderPrivateInstance",
            instance_type="t2.micro",
            image_id=amzn_linux.get_image(self).image_id,
            key_name="demo",
            subnet_id=self.provider_private_subnets[0].ref,
            security_group_ids=[provider_ec2_sg.security_group_id],
            tags=[{"key": "Name", "value": f"{provider_app_prefix}-private-instance"}]
        )

        ### NETWORK LOAD BALANCER SETUP ###
        
        target_group = elbv2.CfnTargetGroup(
            self,
            "ProviderTargetGroup",
            name=f"{provider_app_prefix}-tg",
            port=80,
            protocol="TCP",
            vpc_id=self.provider_vpc.vpc_id,
            target_type="instance",
            health_check_enabled=True,
            health_check_protocol="TCP",
            targets=[
                elbv2.CfnTargetGroup.TargetDescriptionProperty(
                    id=provider_private_instance.ref,
                    port=80
                )
            ]
        )
        
        nlb = elbv2.CfnLoadBalancer(
            self,
            "ProviderNLB",
            name=f"{provider_app_prefix}-nlb",
            type="network",
            scheme="internal",
            subnets=[self.provider_private_subnets[0].ref]
        )
        
        elbv2.CfnListener(
            self,
            "ProviderNLBListener",
            load_balancer_arn=nlb.ref,
            port=80,
            protocol="TCP",
            default_actions=[
                elbv2.CfnListener.ActionProperty(
                    type="forward",
                    target_group_arn=target_group.ref
                )
            ]
        )

        ### VPC ENDPOINT SERVICE ###
        
        vpc_endpoint_service = ec2.CfnVPCEndpointService(
            self,
            "ProviderVpcEndpointService",
            network_load_balancer_arns=[nlb.ref],
            acceptance_required=False
        )
        
        vpc_endpoint = ec2.CfnVPCEndpoint(
            self,
            "ConsumerVpcEndpoint",
            vpc_id=self.consumer_vpc.vpc_id,
            service_name="com.amazonaws.vpce.us-east-1.vpce-svc-02bbd52300b2abe93",
            vpc_endpoint_type="Interface",
            subnet_ids=[self.consumer_private_subnets[0].ref],
            security_group_ids=[consumer_ec2_sg.security_group_id],
            private_dns_enabled=False
        )

        ### OUTPUTS ###
        
        CfnOutput(
            self,
            "VpcEndpointServiceName",
            value=Fn.get_att(vpc_endpoint_service.logical_id, "ServiceId").to_string(),
            description="VPC Endpoint Service Name"
        )
        
        CfnOutput(
            self,
            "NLBDnsName",
            value=nlb.attr_dns_name,
            description="Network Load Balancer DNS Name"
        )