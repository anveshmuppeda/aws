from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)
from constructs import Construct

class HelloWorldL2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function resource
        helloworldfunc = _lambda.Function(
            self, "HelloWorldLambdaFunc",
            runtime=_lambda.Runtime.PYTHON_3_11,
            function_name="HelloWorldFuncL2",
            description="Hello World Lambda Function using L2 Constructs",
            code= _lambda.Code.from_asset("lambda"),
            handler="hello.lambda_handler"
        )

        # Define the API Gateway resource
        restapi = apigateway.LambdaRestApi(
            self, "HelloWorldRestApi",
            rest_api_name= "HelloWorldRestApiL2",
            description="Rest API for Hello World Lambda Func L2",
            handler=helloworldfunc,
            proxy=False,
        )

        # Define the '/hello' resource with a GET method
        hello_resource = restapi.root.add_resource("hello")
        hello_resource.add_method("GET")