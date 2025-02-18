import aws_cdk as core
import aws_cdk.assertions as assertions

from hello_world_l3.hello_world_l3_stack import HelloWorldL3Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in hello_world_l3/hello_world_l3_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = HelloWorldL3Stack(app, "hello-world-l3")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
