import json
import boto3
import requests

def lambda_handler(event, context):
    
    print(event)
    record = event["Records"][0]
    print(record)
    eventType = record["eventName"]
    if eventType == "INSERT":
        print("putting image on s3")
        url = record['dynamodb']['NewImage']['url']['S']
        title = record['dynamodb']['NewImage']['title']['S']
        print(url)
        
        s3 = boto3.client('s3')
        response = s3.list_buckets()    
    
        response = requests.get(url)
        if response.status_code == 200:
            with open("/tmp/image.jpg", 'wb') as f:
                f.write(response.content)
        
        print(str(title) + ".jpg")
        
        with open("/tmp/image.jpg", "rb") as f:
            s3.upload_fileobj(f, "amilosevic-nasa-copy", title + ".jpg")
            
        # TODO implement
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
