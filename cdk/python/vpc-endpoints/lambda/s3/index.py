import boto3

def lambda_handler(event, context):
    try:
        s3 = boto3.client('s3')
        # Attempt to list buckets (this will use the VPC endpoint if configured)
        response = s3.list_buckets()
        bucket_names = [bucket['Name'] for bucket in response.get('Buckets', [])]
        return {
            'statusCode': 200,
            'body': f"Successfully connected to S3. Buckets: {bucket_names}"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Failed to connect to S3 endpoint: {str(e)}"
        }