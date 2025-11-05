#!/usr/bin/env python3

import aws_cdk as cdk

from vpc_endpoint_service.vpc_endpoint_service_stack import VpcEndpointServiceStack


app = cdk.App()
VpcEndpointServiceStack(app, "VpcEndpointServiceStack")

app.synth()
