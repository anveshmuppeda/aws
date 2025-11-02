import json
import boto3

def lambda_handler(event, context):
    ecr_client = boto3.client('ecr')
    
    try:
        response = ecr_client.describe_repositories()
        repositories = response.get('repositories', [])
        
        print(f"Found {len(repositories)} repositories:")
        for repo in repositories:
            print(f"  - {repo['repositoryName']}: {repo['repositoryUri']}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'count': len(repositories),
                'repositories': [
                    {
                        'name': repo['repositoryName'],
                        'uri': repo['repositoryUri']
                    }
                    for repo in repositories
                ]
            }, indent=2)
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }