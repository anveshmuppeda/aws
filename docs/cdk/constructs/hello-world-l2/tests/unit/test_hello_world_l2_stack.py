import aws_cdk as core
import aws_cdk.assertions as assertions

from hello_world_l2.hello_world_l2_stack import HelloWorldL2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in hello_world_l2/hello_world_l2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = HelloWorldL2Stack(app, "hello-world-l2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
