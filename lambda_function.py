import json
from main import main
from reply import reply

def lambda_handler(event, context):
    main()
    reply()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
