from constructs import Construct
from aws_cdk.lambda_layer_kubectl_v30 import KubectlV30Layer
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_eks as eks,
)

class EksClusterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, app_prefix: str, network_stack, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Store network stack reference
        self.network_stack = network_stack

        # Create EKS Service Role
        eks_service_role = iam.Role(
            self,
            "EKSServiceRole",
            role_name=f"{app_prefix}-eks-service-role",
            assumed_by=iam.ServicePrincipal("eks.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEKSClusterPolicy")
            ]
        )

        # Create Node Group Role
        nodegroup_role = iam.Role(
            self,
            "NodeGroupRole",
            role_name=f"{app_prefix}-eks-nodegroup-role",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEKSWorkerNodePolicy"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEKS_CNI_Policy"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEC2ContainerRegistryReadOnly"),
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonEBSCSIDriverPolicy")
            ]
        )

        # Create masters role for testing - WIDE OPEN ACCESS
        masters_role = iam.Role(
            self,
            "EKSMastersRole",
            role_name=f"{app_prefix}-eks-masters-role",
            assumed_by=iam.CompositePrincipal(
                iam.AccountRootPrincipal(),
                iam.AnyPrincipal(),  # WARNING: This allows ANYONE to assume this role
            ),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")  # WARNING: Full admin access
            ]
        )

        # Convert CFN subnets to ISubnet objects that EKS can use
        private_subnets = []
        for i, cfn_subnet in enumerate(network_stack.private_subnets):
            subnet = ec2.Subnet.from_subnet_attributes(
                self,
                f"PrivateSubnet{i+1}Import",
                subnet_id=cfn_subnet.ref,
                availability_zone=cfn_subnet.availability_zone,
                route_table_id=network_stack.private_route_table.ref
            )
            private_subnets.append(subnet)

        public_subnets = []
        for i, cfn_subnet in enumerate(network_stack.public_subnets):
            subnet = ec2.Subnet.from_subnet_attributes(
                self,
                f"PublicSubnet{i+1}Import",
                subnet_id=cfn_subnet.ref,
                availability_zone=cfn_subnet.availability_zone,
                route_table_id=network_stack.public_route_table.ref
            )
            public_subnets.append(subnet)

        # Create VPC selection for EKS
        vpc_subnets = [
            ec2.SubnetSelection(subnets=private_subnets),
            ec2.SubnetSelection(subnets=public_subnets)
        ]

        # Create EKS Cluster - WITH masters_role for testing
        self.cluster = eks.Cluster(
            self,
            "EKSCluster",
            cluster_name=f"{app_prefix}-eks-cluster",
            version=eks.KubernetesVersion.V1_30,
            vpc=network_stack.vpc,
            vpc_subnets=vpc_subnets,
            role=eks_service_role,
            masters_role=masters_role,  # Using the admin role
            kubectl_layer=KubectlV30Layer(self, "kubectl"),
            default_capacity=0,
            endpoint_access=eks.EndpointAccess.PUBLIC_AND_PRIVATE,
            cluster_logging=[
                eks.ClusterLoggingTypes.API,
                eks.ClusterLoggingTypes.AUTHENTICATOR,
                eks.ClusterLoggingTypes.SCHEDULER,
                eks.ClusterLoggingTypes.AUDIT,
                eks.ClusterLoggingTypes.CONTROLLER_MANAGER,
            ],
        )

        # Add node groups and addons
        self.__add_nodegroup(cluster=self.cluster, nodegroup_role=nodegroup_role, app_prefix=app_prefix)
        self.__add_addon(cluster=self.cluster)

    def __add_nodegroup(self, cluster: eks.Cluster, nodegroup_role: iam.Role, app_prefix: str):
        instance_type_name = "t3.medium"

        # Create managed node group in private subnets
        self.nodegroup = eks.Nodegroup(
            self,
            "PrimaryNodeGroup",
            cluster=cluster,
            nodegroup_name=f"{app_prefix}-primary-nodegroup",
            node_role=nodegroup_role,
            instance_types=[ec2.InstanceType(instance_type_name)],
            subnets=ec2.SubnetSelection(
                subnets=[
                    ec2.Subnet.from_subnet_attributes(
                        self,
                        f"NodeGroupSubnet{i+1}",
                        subnet_id=cfn_subnet.ref,
                        availability_zone=cfn_subnet.availability_zone
                    ) for i, cfn_subnet in enumerate(self.network_stack.private_subnets)
                ]
            ),
            min_size=1,
            max_size=5,
            desired_size=2,
            disk_size=100,
            ami_type=eks.NodegroupAmiType.AL2_X86_64,
            capacity_type=eks.CapacityType.ON_DEMAND,
            labels={
                "instance-type": instance_type_name,
                "nodegroup-type": "primary"
            },
            tags={
                "Name": f"{app_prefix}-primary-nodegroup",
                "Environment": "testing"  # Changed to reflect testing nature
            }
        )

    def __add_addon(self, cluster: eks.Cluster):
        # VPC CNI Addon
        eks.CfnAddon(
            self,
            "VPCCNIAddon",
            addon_name="vpc-cni",
            cluster_name=cluster.cluster_name,
            addon_version="v1.18.1-eksbuild.1",
            resolve_conflicts="OVERWRITE"
        )
        
        # CoreDNS Addon
        eks.CfnAddon(
            self,
            "CoreDNSAddon",
            addon_name="coredns",
            cluster_name=cluster.cluster_name,
            addon_version="v1.11.1-eksbuild.4",
            resolve_conflicts="OVERWRITE"
        )
        
        # Kube Proxy Addon
        eks.CfnAddon(
            self,
            "KubeProxyAddon",
            addon_name="kube-proxy",
            cluster_name=cluster.cluster_name,
            addon_version="v1.30.0-eksbuild.3",
            resolve_conflicts="OVERWRITE"
        )
        
        # EBS CSI Driver Addon
        eks.CfnAddon(
            self,
            "EBSCSIDriverAddon",
            addon_name="aws-ebs-csi-driver",
            cluster_name=cluster.cluster_name,
            addon_version="v1.31.0-eksbuild.1",
            resolve_conflicts="OVERWRITE"
        )