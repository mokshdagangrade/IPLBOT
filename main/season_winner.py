import json
import boto3

s3=boto3.client('s3')

def lambda_handler(event,context):
    year = event['currentIntent']['slots']['year']
    bucket='ipldata'
    key='data.json'
    response=s3.get_object(Bucket=bucket,Key=key)
    content = response['Body']
    jsonObject=json.loads(content.read())
    year1=jsonObject[year]
   
    for i in year1:
        l=len(year1)
        str= year1[l-1]['winner']
        x=str.replace(" "," ")
    
    response={
         "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "PlainText",
              "content": "{w} is the winner".format(w=x)
            }   ,
             
         }
    }
    return response
    
    
    
        

    
