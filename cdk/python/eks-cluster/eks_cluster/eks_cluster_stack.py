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

        # Create masters role for kubectl access
        masters_role = iam.Role(
            self,
            "EKSMastersRole",
            role_name=f"{app_prefix}-eks-masters-role",
            assumed_by=iam.CompositePrincipal(
                iam.AccountRootPrincipal(),  # Allow root account access
            ),
        )
        masters_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEKSClusterPolicy")
        )

        # Create readonly role
        readonly_role = iam.Role(
            self,
            "EKSReadOnlyRole",
            role_name=f"{app_prefix}-eks-readonly-role",
            assumed_by=iam.CompositePrincipal(
                iam.AccountRootPrincipal(),
            ),
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

        # Create EKS Cluster
        self.cluster = eks.Cluster(
            self,
            "EKSCluster",
            cluster_name=f"{app_prefix}-eks-cluster",
            version=eks.KubernetesVersion.V1_30,  # Fixed: V1_32 doesn't exist, use V1_30
            vpc=network_stack.vpc,
            vpc_subnets=vpc_subnets,
            role=eks_service_role,
            masters_role=masters_role,
            kubectl_layer=KubectlV30Layer(self, "kubectl"),
            default_capacity=0,  # We'll add managed node groups separately
            endpoint_access=eks.EndpointAccess.PUBLIC_AND_PRIVATE,
            cluster_logging=[
                eks.ClusterLoggingTypes.API,
                eks.ClusterLoggingTypes.AUTHENTICATOR,
                eks.ClusterLoggingTypes.SCHEDULER,
                eks.ClusterLoggingTypes.AUDIT,
                eks.ClusterLoggingTypes.CONTROLLER_MANAGER,
            ],
        )

        # Grant masters role access to the cluster
        masters_role.grant_assume_role(self.cluster.admin_role)

        # Add readonly role mapping
        self.cluster.aws_auth.add_role_mapping(
            readonly_role, 
            groups=["system:authenticated"]
        )

        # Add node groups, addons, and RBAC
        self.__add_nodegroup(cluster=self.cluster, nodegroup_role=nodegroup_role, app_prefix=app_prefix)
        self.__add_addon(cluster=self.cluster)
        self.__add_readonly_member(
            cluster=self.cluster, 
            readonly_role_arn=readonly_role.role_arn
        )

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
            min_size=1,  # Reduced min_size to 1 for cost savings
            max_size=5,
            desired_size=2,  # Reduced desired_size to 2 for cost savings
            disk_size=100,
            ami_type=eks.NodegroupAmiType.AL2_X86_64,
            capacity_type=eks.CapacityType.ON_DEMAND,
            labels={
                "instance-type": instance_type_name,
                "nodegroup-type": "primary"
            },
            tags={
                "Name": f"{app_prefix}-primary-nodegroup",
                "Environment": "production"
            }
        )

    def __add_addon(self, cluster: eks.Cluster):
        # VPC CNI Addon - Updated to compatible version
        eks.CfnAddon(
            self,
            "VPCCNIAddon",
            addon_name="vpc-cni",
            cluster_name=cluster.cluster_name,
            addon_version="v1.18.1-eksbuild.1",  # Updated for K8s 1.30 compatibility
            resolve_conflicts="OVERWRITE"
        )
        
        # CoreDNS Addon - Updated to compatible version
        eks.CfnAddon(
            self,
            "CoreDNSAddon",
            addon_name="coredns",
            cluster_name=cluster.cluster_name,
            addon_version="v1.11.1-eksbuild.4",  # Updated for K8s 1.30 compatibility
            resolve_conflicts="OVERWRITE"
        )
        
        # Kube Proxy Addon - Updated to compatible version
        eks.CfnAddon(
            self,
            "KubeProxyAddon",
            addon_name="kube-proxy",
            cluster_name=cluster.cluster_name,
            addon_version="v1.30.0-eksbuild.3",  # Updated for K8s 1.30 compatibility
            resolve_conflicts="OVERWRITE"
        )
        
        # EBS CSI Driver Addon - Updated to compatible version
        eks.CfnAddon(
            self,
            "EBSCSIDriverAddon",
            addon_name="aws-ebs-csi-driver",
            cluster_name=cluster.cluster_name,
            addon_version="v1.31.0-eksbuild.1",  # Updated for K8s 1.30 compatibility
            resolve_conflicts="OVERWRITE"
        )

    def __add_readonly_member(self, cluster: eks.Cluster, readonly_role_arn: str):
        # Create ClusterRole for readonly access
        cluster.add_manifest(
            "ReadOnlyClusterRole",
            {
                "apiVersion": "rbac.authorization.k8s.io/v1",
                "kind": "ClusterRole",
                "metadata": {
                    "name": "eks-readonly-cluster-role",
                },
                "rules": [
                    {
                        "apiGroups": [""],
                        "resources": [
                            "configmaps",
                            "services",
                            "pods",
                            "persistentvolumes",
                            "persistentvolumeclaims",
                            "namespaces",
                            "nodes",
                            "events"
                        ],
                        "verbs": ["get", "list", "watch"],
                    },
                    {
                        "apiGroups": [""],
                        "resources": ["pods/log"],
                        "verbs": ["get", "list"],
                    },
                    {
                        "apiGroups": [""],
                        "resources": ["pods/portforward", "services/portforward"],
                        "verbs": ["create"],
                    },
                    {
                        "apiGroups": ["apps"],
                        "resources": [
                            "deployments",
                            "daemonsets",
                            "replicasets",
                            "statefulsets"
                        ],
                        "verbs": ["get", "list", "watch"],
                    },
                    {
                        "apiGroups": ["extensions"],
                        "resources": ["deployments", "replicasets"],
                        "verbs": ["get", "list", "watch"],
                    }
                ],
            },
        )

        # Create ClusterRoleBinding
        cluster.add_manifest(
            "ReadOnlyClusterRoleBinding",
            {
                "apiVersion": "rbac.authorization.k8s.io/v1",
                "kind": "ClusterRoleBinding",
                "metadata": {
                    "name": "eks-readonly-cluster-role-binding",
                },
                "roleRef": {
                    "apiGroup": "rbac.authorization.k8s.io",
                    "kind": "ClusterRole",
                    "name": "eks-readonly-cluster-role",
                },
                "subjects": [
                    {
                        "kind": "User",
                        "name": readonly_role_arn,
                        "apiGroup": "rbac.authorization.k8s.io",
                    }
                ],
            },
        )