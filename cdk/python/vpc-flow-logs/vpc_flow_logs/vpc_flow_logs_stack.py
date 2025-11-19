from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_logs as logs,
    RemovalPolicy
)


class VpcFlowLogsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        app_prefix = "vpc-flowlogs-demo"

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

        ### VPC FLOW LOGS SETUP ###
        
        # Create CloudWatch Log Group for VPC Flow Logs
        flow_logs_log_group = logs.LogGroup(
            self,
            "VPCFlowLogsLogGroup",
            log_group_name=f"/aws/vpc/flowlogs/{app_prefix}",
            retention=logs.RetentionDays.ONE_WEEK,  # Adjust retention as needed
            removal_policy=RemovalPolicy.DESTROY  # For demo purposes; use RETAIN in production
        )
        
        # Create IAM Role for VPC Flow Logs
        flow_logs_role = iam.Role(
            self,
            "VPCFlowLogsRole",
            assumed_by=iam.ServicePrincipal("vpc-flow-logs.amazonaws.com"),
            description="Role for VPC Flow Logs to write to CloudWatch"
        )
        
        # Attach policy to allow writing to CloudWatch Logs
        flow_logs_role.add_to_policy(
            iam.PolicyStatement(
                actions=[
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                    "logs:DescribeLogGroups",
                    "logs:DescribeLogStreams"
                ],
                resources=[flow_logs_log_group.log_group_arn]
            )
        )
        
        # Enable VPC Flow Logs
        ec2.CfnFlowLog(
            self,
            "VPCFlowLog",
            resource_type="VPC",
            resource_id=self.demo_vpc.vpc_id,
            traffic_type="ALL",  # Options: ACCEPT, REJECT, or ALL
            log_destination_type="cloud-watch-logs",
            log_destination=flow_logs_log_group.log_group_arn,
            deliver_logs_permission_arn=flow_logs_role.role_arn,
            # Optional: Custom log format (default format shown below)
            # log_format="${version} ${account-id} ${interface-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${packets} ${bytes} ${start} ${end} ${action} ${log-status}",
            tags=[{"key": "Name", "value": f"{app_prefix}-flow-log"}]
        )
        
        ### END VPC FLOW LOGS SETUP ###
        
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
            internet_gateway_id=self.igw.ref
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
            route_table_id=self.public_route_table.ref,
            destination_cidr_block="0.0.0.0/0",
            gateway_id=self.igw.ref
        )
        
        # Associate public subnets with public route table
        for i, subnet in enumerate(self.public_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"PublicSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,
                route_table_id=self.public_route_table.ref
            )
        
        # Private Route Table
        self.private_route_table = ec2.CfnRouteTable(
            self,
            "PrivateRouteTable",
            vpc_id=self.demo_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{app_prefix}-private-rt"}]
        )
        
        # Associate private subnets with private route table
        for i, subnet in enumerate(self.private_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"PrivateSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,
                route_table_id=self.private_route_table.ref
            )
        
        ### SECURITY GROUPS ###
        
        # Create Security Group for Public EC2 instances
        public_ec2_sg = ec2.SecurityGroup(
            self,
            "PublicEC2SecurityGroup",
            vpc=self.demo_vpc,
            security_group_name=f"{app_prefix}-public-ec2-sg",
            description="Security group for Public EC2 instances",
            allow_all_outbound=True
        )
        
        public_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH from anywhere"
        )
        
        # Create Security Group for Private EC2 instances
        private_ec2_sg = ec2.SecurityGroup(
            self,
            "PrivateEC2SecurityGroup",
            vpc=self.demo_vpc,
            security_group_name=f"{app_prefix}-private-ec2-sg",
            description="Security group for Private EC2 instances",
            allow_all_outbound=True
        )
        
        private_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH from anywhere"
        )
        
        private_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.20.0.0/16"),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP from Private VPC"
        )

        ### EC2 INSTANCES ###
        
        amzn_linux = ec2.MachineImage.latest_amazon_linux2023(
            edition=ec2.AmazonLinuxEdition.STANDARD,
            cpu_type=ec2.AmazonLinuxCpuType.X86_64
        )
        
        # instances (one public, one private)
        ec2.CfnInstance(
            self,
            "PublicInstance",
            instance_type="t2.micro",
            image_id=amzn_linux.get_image(self).image_id,
            key_name="demo",
            subnet_id=self.public_subnets[0].ref,
            security_group_ids=[public_ec2_sg.security_group_id],
            tags=[{"key": "Name", "value": f"{app_prefix}-public-instance"}]
        )
        
        ec2.CfnInstance(
            self,
            "PrivateInstance",
            instance_type="t2.micro",
            image_id=amzn_linux.get_image(self).image_id,
            key_name="demo",
            subnet_id=self.private_subnets[0].ref,
            security_group_ids=[private_ec2_sg.security_group_id],
            tags=[{"key": "Name", "value": f"{app_prefix}-private-instance"}]
        )