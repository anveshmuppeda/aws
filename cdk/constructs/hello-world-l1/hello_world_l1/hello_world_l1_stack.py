from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,

)
from constructs import Construct
import os

class HelloWorldL1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        helloworldfunc = _lambda.CfnFunction(self, "HelloWorldFunc",
            function_name="HelloWorldFuncL1",
            description= "Hello World Func using L1 Constructs",
            code=_lambda.CfnFunction.CodeProperty(
                zip_file=open("lambda/hello.py", "r").read()
            ),
            # When you use the inline zip_file property, AWS Lambda treats the provided code as if it were in a file named index.py by default. To preserve your file name (i.e. keep it as hello.py), you need to package your code as an asset (a zip file) rather than using inline code.
            # Since it is inline i am using index instead of hello
            handler="index.lambda_handler",
            runtime="python3.11",
            # Lambda Execution Role
            role="arn:aws:iam::463470985368:role/HelloWorldLambdaExecutionRole"
        )

        restapi = apigateway.CfnRestApi(self, "MyRestAPI",
            name="HelloWorldRestApiL1",
            description="Rest API for Hello World Lambda Func L1",
            endpoint_configuration=apigateway.CfnRestApi.EndpointConfigurationProperty(
                types=["REGIONAL"]
            )
        )

        # Get the root resource ID of the API
        root_resource_id = restapi.attr_root_resource_id

        # Create a resource (/hello)
        hello_resource = apigateway.CfnResource(
            self, "HelloResource",
            parent_id=root_resource_id,
            path_part="hello",
            rest_api_id=restapi.ref
        )

        # Create a GET method for /hello and integrate with Lambda
        hello_method = apigateway.CfnMethod(
            self, "HelloGETMethod",
            rest_api_id=restapi.ref,
            resource_id=hello_resource.ref,
            http_method="GET",
            authorization_type="NONE",
            integration=apigateway.CfnMethod.IntegrationProperty(
                type="AWS_PROXY",
                integration_http_method="POST",
                uri=f"arn:aws:apigateway:{self.region}:lambda:path/2015-03-31/functions/{helloworldfunc.attr_arn}/invocations"
            )
        )

        # Grant API Gateway permission to invoke Lambda
        lambda_permissions = _lambda.CfnPermission(
            self, "LambdaPermissions",
            action="lambda:InvokeFunction",
            function_name=helloworldfunc.ref,
            principal="apigateway.amazonaws.com",
            source_arn=f"arn:aws:execute-api:{self.region}:{self.account}:{restapi.ref}/*/*"
        )

        # Create a deployment and stage for the API
        deployment = apigateway.CfnDeployment(
            self, "Deployment",
            rest_api_id=restapi.ref
        )

        stage = apigateway.CfnStage(
            self, "Stage",
            rest_api_id=restapi.ref,
            deployment_id=deployment.ref,
            stage_name="dev"
        )
