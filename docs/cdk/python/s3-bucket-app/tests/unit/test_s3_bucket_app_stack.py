import aws_cdk as core
import aws_cdk.assertions as assertions
from s3_bucket_app.s3_bucket_app_stack import S3BucketAppStack


def test_sqs_queue_created():
    app = core.App()
    stack = S3BucketAppStack(app, "s3-bucket-app")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = S3BucketAppStack(app, "s3-bucket-app")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
