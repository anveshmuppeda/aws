from aws_cdk import (
    Stack,
    aws_secretsmanager as secretsmanager,
    SecretValue,
    CfnParameter
)
from constructs import Construct

class MySecretCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a CloudFormation parameter for the certificate
        certificate_param = CfnParameter(self, 'CertificateParam',
            type='String',  # Use 'String' (capital S)
            no_echo=True,  # Ensures the value is not displayed
            description='The certificate to be stored in Secrets Manager'
        )

        # Create a secret using the certificate content passed as a parameter
        cert_secret = secretsmanager.Secret(self, "MyCertificateSecret",
            secret_string_value=SecretValue.unsafe_plain_text(certificate_param.value_as_string)
        )
