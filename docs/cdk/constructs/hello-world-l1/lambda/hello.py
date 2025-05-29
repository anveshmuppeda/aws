import json

def lambda_handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, from Lambda L1 Construct! You have hit {}\n'.format(event['path'])
    }