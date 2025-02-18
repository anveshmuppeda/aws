#!/usr/bin/env python3
import os

import aws_cdk as cdk

from hello_world_l1.hello_world_l1_stack import HelloWorldL1Stack


app = cdk.App()
HelloWorldL1Stack(app, "HelloWorldL1Stack")

app.synth()
