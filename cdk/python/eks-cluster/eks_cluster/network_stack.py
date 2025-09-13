from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
    Stack,
)

class NetworkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, app_prefix: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Create VPC
        self.vpc = ec2.Vpc(
            self,
            "VPC",
            vpc_name=f"{app_prefix}-vpc",
            ip_addresses=ec2.IpAddresses.cidr("10.10.0.0/16"),
            enable_dns_hostnames=True,
            enable_dns_support=True,
            # Create VPC without subnets
            subnet_configuration=[]
        )
        
        # Get availability zones (first 2)
        azs = self.availability_zones[:2]
        
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
            vpc_id=self.vpc.vpc_id,
            internet_gateway_id=self.igw.attr_internet_gateway_id
        )
        
        # Create Public Subnets
        self.public_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"PublicSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.10.{i}.0/24",
                vpc_id=self.vpc.vpc_id,
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
                vpc_id=self.vpc.vpc_id,
                map_public_ip_on_launch=False,
                tags=[{"key": "Name", "value": f"{app_prefix}-private-subnet-{i+1}"}]
            )
            self.private_subnets.append(subnet)
        
        # Create NAT Gateway (in first public subnet)
        self.nat_gateway = ec2.CfnNatGateway(
            self,
            "NATGateway",
            subnet_id=self.public_subnets[0].attr_subnet_id,
            allocation_id=ec2.CfnEIP(
                self,
                "NATGatewayEIP",
                domain="vpc",
                tags=[{"key": "Name", "value": f"{app_prefix}-nat-eip"}]
            ).attr_allocation_id,
            tags=[{"key": "Name", "value": f"{app_prefix}-nat-gateway"}]
        )
        
        # Create Route Tables
        # Public Route Table
        self.public_route_table = ec2.CfnRouteTable(
            self,
            "PublicRouteTable",
            vpc_id=self.vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{app_prefix}-public-rt"}]
        )
        
        # Add route to Internet Gateway
        ec2.CfnRoute(
            self,
            "PublicRoute",
            route_table_id=self.public_route_table.attr_route_table_id,
            destination_cidr_block="0.0.0.0/0",
            gateway_id=self.igw.attr_internet_gateway_id
        )
        
        # Associate public subnets with public route table
        for i, subnet in enumerate(self.public_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"PublicSubnetRTAssoc{i+1}",
                subnet_id=subnet.attr_subnet_id,
                route_table_id=self.public_route_table.attr_route_table_id
            )
        
        # Private Route Table
        self.private_route_table = ec2.CfnRouteTable(
            self,
            "PrivateRouteTable",
            vpc_id=self.vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{app_prefix}-private-rt"}]
        )
        
        # Add route to NAT Gateway
        ec2.CfnRoute(
            self,
            "PrivateRoute",
            route_table_id=self.private_route_table.attr_route_table_id,
            destination_cidr_block="0.0.0.0/0",
            nat_gateway_id=self.nat_gateway.attr_nat_gateway_id
        )
        
        # Associate private subnets with private route table
        for i, subnet in enumerate(self.private_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"PrivateSubnetRTAssoc{i+1}",
                subnet_id=subnet.attr_subnet_id,
                route_table_id=self.private_route_table.attr_route_table_id
            )
        
        # Create NACL for Public Subnets
        self.public_nacl = ec2.NetworkAcl(
            self,
            "PublicNACL",
            vpc=self.vpc,
            network_acl_name=f"{app_prefix}-public-nacl"
        )
        
        # Public NACL Rules - Allow common web traffic
        # Inbound Rules
        self.public_nacl.add_entry(
            "AllowInboundHTTP",
            rule_number=100,
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        self.public_nacl.add_entry(
            "AllowInboundHTTPS", 
            rule_number=110,
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        self.public_nacl.add_entry(
            "AllowInboundSSH",
            rule_number=120,
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        # Allow ephemeral ports for return traffic
        self.public_nacl.add_entry(
            "AllowInboundEphemeral",
            rule_number=130,
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        # Outbound Rules - Allow all outbound traffic
        self.public_nacl.add_entry(
            "AllowAllOutbound",
            rule_number=100,
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        # Create NACL for Private Subnets
        self.private_nacl = ec2.NetworkAcl(
            self,
            "PrivateNACL",
            vpc=self.vpc,
            network_acl_name=f"{app_prefix}-private-nacl"
        )
        
        # Private NACL Rules - More restrictive
        # Allow inbound from VPC CIDR
        self.private_nacl.add_entry(
            "AllowInboundFromVPC",
            rule_number=100,
            cidr=ec2.AclCidr.ipv4("10.10.0.0/16"),
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        # Allow ephemeral ports for return traffic from internet
        self.private_nacl.add_entry(
            "AllowInboundEphemeral",
            rule_number=110,
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        # Allow outbound to VPC CIDR
        self.private_nacl.add_entry(
            "AllowOutboundToVPC",
            rule_number=100,
            cidr=ec2.AclCidr.ipv4("10.10.0.0/16"),
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        # Allow outbound HTTP/HTTPS for updates and downloads
        self.private_nacl.add_entry(
            "AllowOutboundHTTP",
            rule_number=110,
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        self.private_nacl.add_entry(
            "AllowOutboundHTTPS",
            rule_number=120,
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        # Allow outbound DNS
        self.private_nacl.add_entry(
            "AllowOutboundDNS",
            rule_number=130,
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.udp_port(53),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        # Associate NACLs with subnets
        for i, subnet in enumerate(self.public_subnets):
            ec2.SubnetNetworkAclAssociation(
                self,
                f"PublicSubnetNACLAssoc{i}",
                subnet=subnet.attr_subnet_id,
                network_acl=self.public_nacl.network_acl_id
            )
            
        for i, subnet in enumerate(self.private_subnets):
            ec2.SubnetNetworkAclAssociation(
                self,
                f"PrivateSubnetNACLAssoc{i}",
                subnet=subnet.attr_subnet_id,
                network_acl=self.private_nacl.network_acl_id
            )
        
        # Export important values for other stacks
        self.vpc_id = self.vpc.vpc_id
        self.public_subnet_ids = [subnet.attr_subnet_id for subnet in self.public_subnets]
        self.private_subnet_ids = [subnet.attr_subnet_id for subnet in self.private_subnets]