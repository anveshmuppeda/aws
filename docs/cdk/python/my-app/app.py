#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_app.my_app_stack import MyAppStack


app = cdk.App()
MyAppStack(app, "MyAppStack")

app.synth()
