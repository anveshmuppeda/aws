#!/usr/bin/env python3

import aws_cdk as cdk

from eks_cluster.eks_cluster_stack import EksClusterStack
from eks_cluster.network_stack import NetworkStack

app = cdk.App()

network_stack = NetworkStack(app, "NetworkStack")
eks_stack = EksClusterStack(app, "EksClusterStack")

app.synth()
