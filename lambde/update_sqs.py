import json
import boto3

def lambda_handler(event, context):
    print(event)
    record = event["Records"][0]
    print(record)
    eventType = record['eventName']
    if eventType == 'MODIFY':
        print('record modified, sending message to sqs')
        obj = record['dynamodb']['NewImage']
        print(obj)
        title = obj['title']['S']
        url = obj['url']['S']
        internal_url = obj['internal_url']['S']
        sqs = boto3.client('sqs')
        message = 'The image ' + str(title) + ' has been created on s3 with url: ' + str(internal_url) + '!'
        print(message)
        
        sqs.send_message(
                QueueUrl='amilosevic-queue',
                MessageBody=message,
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
