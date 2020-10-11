import json
import boto3

s3=boto3.client('s3')

def lambda_handler(event,context):
    year = event['currentIntent']['slots']['year']
    teamA = event['currentIntent']['slots']['TeamA']
    teamB = event['currentIntent']['slots']['TeamB']
    bucket='ipldata'
    key='data.json'
    response=s3.get_object(Bucket=bucket,Key=key)
    content = response['Body']
    jsonObject=json.loads(content.read())
    year1=jsonObject[year]
    
    
    for i in year1:
        if(teamA==i['team1'] and teamB==i['team2']):
            str=i['winner']
            x=str.replace(" "," ")
            yr=i['season']
            aa=i['win_by_wickets']
            bb=i['win_by_runs']
        
    response={
        "sessionAttributes": {
            "key":"{j}".format(j=yr)
        },
         "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "PlainText",
              "content": "{w} won by {a} wickets and {b} runs".format(w=x,a=aa,b=bb)
            }   ,
             
         }
    }
    return response 
