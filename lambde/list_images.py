import json
import boto3
import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    bucket_name = 'amilosevic-nasa-copy'
    now = datetime.datetime.now(datetime.timezone.utc)
    objects = s3.list_objects(Bucket = bucket_name)
    for i in objects['Contents']:
        key = i['Key']
        lastMod = i['LastModified']
        delta = now - lastMod
        days = delta.days
        if days < 7 and key.endswith(".jpg"):
            print('Access the image on: ' + 's3://' + str(bucket_name) + '/' + str(key))
        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
