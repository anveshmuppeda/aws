#!/usr/bin/env python3

import aws_cdk as cdk

from s3_bucket_app.s3_bucket_app_stack import S3BucketAppStack


app = cdk.App()
S3BucketAppStack(app, "S3BucketAppStack")

app.synth()
