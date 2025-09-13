#!/usr/bin/env python3

import aws_cdk as cdk
from aws_cdk import Tags

from eks_cluster.eks_cluster_stack import EksClusterStack
from eks_cluster.network_stack import NetworkStack

app = cdk.App()

APP_PREFIX = "eks-demo"

network_stack = NetworkStack(app, "NetworkStack", app_prefix=APP_PREFIX)
eks_stack = EksClusterStack(app, "EksClusterStack")

Tags.of(app).add("Application", "eks-demo")

app.synth()