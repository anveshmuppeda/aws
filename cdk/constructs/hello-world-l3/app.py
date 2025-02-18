#!/usr/bin/env python3
import os

import aws_cdk as cdk

from hello_world_l3.hello_world_l3_stack import HelloWorldL3Stack

app = cdk.App()
HelloWorldL3Stack(app, "HelloWorldL3Stack")

app.synth()
