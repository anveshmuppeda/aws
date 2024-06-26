import boto3

def lambda_handler(event, context):
    # Initialize EC2 client
    ec2_client = boto3.client('ec2')

    # Specify parameters for the instance
    instance_params = {
        'ImageId': 'ami-053b0d53c279acc90',
        'InstanceType': 't2.micro',
        'MinCount': 1,  # Minimum number of instances to launch
        'MaxCount': 1,   # Maximum number of instances to launch
        'TagSpecifications': [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'FromAWSLambda'  # Specify the desired name for your instance here
                    }
                ]
            }
        ]
    }

    # Launch the instance
    response = ec2_client.run_instances(**instance_params)

    # Extract instance ID from the response
    instance_id = response['Instances'][0]['InstanceId']

    return {
        'statusCode': 200,
        'body': f'EC2 instance {instance_id} has been launched.'
    }
