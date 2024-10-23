from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_secretsmanager as secretsmanager,
)
from constructs import Construct

class MySecretCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a simple secret with a username and generated password
        simple_secret = secretsmanager.Secret(self, "MySimpleSecret",
            generate_secret_string=secretsmanager.SecretStringGenerator(
                secret_string_template='{"username": "myUsername"}',  # Predefined username
                generate_string_key="password",  # Key for generated password
                #generate_string_key_2="LoginPassword",
                exclude_characters="/@\"'"  # Characters to exclude from password
            )
        )
