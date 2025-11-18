#!/usr/bin/env python3

import aws_cdk as cdk

from vpc_flow_logs.vpc_flow_logs_stack import VpcFlowLogsStack


app = cdk.App()
VpcFlowLogsStack(app, "VpcFlowLogsStack")

app.synth()
