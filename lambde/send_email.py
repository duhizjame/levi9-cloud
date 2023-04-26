import json

import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):
    print(event)
    record = event["Records"][0]
    print(record)
    message = record["body"]
    
    ses.send_email(
         Destination={
        'ToAddresses': [
            'aleksandarmilosevic98@gmail.com'
        ],
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': message,
            },
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'Test email',
        },
    },
    Source='aleksandarmilosevic98@gmail.com'
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
