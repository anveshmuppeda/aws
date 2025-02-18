from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    App
)

from aws_solutions_constructs import (
    aws_apigateway_lambda as apigw_lambda
)

from constructs import Construct

class HelloWorldL3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        apiGatewaytoLambda = apigw_lambda.ApiGatewayToLambda(
            self, "ApiGatewayToLambda",
            lambda_function_props=_lambda.FunctionProps(
                runtime=_lambda.Runtime.PYTHON_3_13,
                code=_lambda.Code.from_asset('lambda'),
                handler='hello.lambda_handler',
                function_name="HelloWorldFuncL3"
            ),
            api_gateway_props= apigateway.RestApiProps(
                rest_api_name="HelloWorldRestApiL3",
                description="Rest Api for Hello World Lambda Func L3",
                default_method_options=apigateway.MethodOptions(
                    authorization_type=apigateway.AuthorizationType.NONE
            )
        )
        )