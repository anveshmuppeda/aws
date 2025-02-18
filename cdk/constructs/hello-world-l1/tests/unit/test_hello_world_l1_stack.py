import aws_cdk as core
import aws_cdk.assertions as assertions

from hello_world_l1.hello_world_l1_stack import HelloWorldL1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in hello_world_l1/hello_world_l1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = HelloWorldL1Stack(app, "hello-world-l1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
