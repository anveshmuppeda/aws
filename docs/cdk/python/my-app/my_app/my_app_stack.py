from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class MyAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_vpc = ec2.CfnVPC(self, 'MyPublicVpc',
                            cidr_block='10.0.0.0/16',
                            enable_dns_hostnames=True,
                            enable_dns_support=True,
                            )
        
        internet_gateway = ec2.CfnInternetGateway(self, "MyIntergatway1")

        ec2.CfnVPCGatewayAttachment(self, 'MyIGAttattachment',
                                    vpc_id=my_vpc.attr_vpc_id,
                                    internet_gateway_id=internet_gateway.attr_internet_gateway_id)
        
        my_subnets = [
            { 'cidr_block': '10.0.0.0/24', 'public': True },
            { 'cidr_block': '10.0.0.1/24', 'public': True },
            { 'cidr_block': '10.0.0.2/24', 'public': False },
            { 'cidr_block': '10.0.0.3/24', 'public': False },
        ]

        for i,subnet in enumerate(my_subnets):
            subnet_resource = ec2.CfnSubnet(self, f'Subnet{i+1}',
                                            vpc_id=my_vpc.attr_vpc_id,
                                            cidr_block=subnet['cidr_block'],
                                            map_public_ip_on_launch=subnet['public'],
                                            availability_zone=Stack.availability_zones.fget(self)[i%2])
            
            route_table = ec2.CfnRouteTable(self, f'Subnet{i+1}RoutTable',
                                            vpc_id=my_vpc.attr_vpc_id)
            
            ec2.CfnSubnetRouteTableAssociation(self, f'Subnet{i+1}RouteTableAsscn',
                                               route_table_id=route_table.attr_route_table_id,
                                               subnet_id=subnet_resource.attr_subnet_id)
            
            if subnet['public']:
                ec2.CfnRoute(self, f'Subenet{i+1}InternetRoute',
                             route_table_id=route_table.attr_route_table_id,
                             destination_cidr_block='0.0.0.0/0',
                             gateway_id=internet_gateway.attr_internet_gateway_id)
        