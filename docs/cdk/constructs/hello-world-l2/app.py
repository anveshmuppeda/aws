#!/usr/bin/env python3
import os
import aws_cdk as cdk

from hello_world_l2.hello_world_l2_stack import HelloWorldL2Stack

app = cdk.App()
HelloWorldL2Stack(app, "HelloWorldL2Stack")

app.synth()
