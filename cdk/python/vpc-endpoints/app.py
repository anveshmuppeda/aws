#!/usr/bin/env python3

import aws_cdk as cdk

from vpc_endpoints.vpc_endpoints_stack import VpcEndpointsStack


app = cdk.App()
VpcEndpointsStack(app, "VpcEndpointsStack")

app.synth()
