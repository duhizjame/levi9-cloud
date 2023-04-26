import json
import boto3

def lambda_handler(event, context):
    print(event)
    record = event["Records"][0]
    print(record)
    obj = record['s3']['object']
    bucket = record['s3']['bucket']['name']
    key = obj['key']
    
    internal_url = 'https://' + str(bucket)  + '.s3.amazonaws.com' + '/' + str(key)
    print(internal_url)

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('amilosevic-nasa-2')
    dynamoId = key.replace("+", " ").split(".")[0]
    print(dynamoId)

    table.update_item(
        Key={
            'title': dynamoId
            },
        UpdateExpression='SET internal_url = :val1',
        ExpressionAttributeValues={
        ':val1': internal_url
            }
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
