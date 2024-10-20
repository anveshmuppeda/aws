#!/usr/bin/env python3

import aws_cdk as cdk

from first_cdk_app.first_cdk_app_stack import FirstCdkAppStack


app = cdk.App()
FirstCdkAppStack(app, "FirstCdkAppStack")

app.synth()
