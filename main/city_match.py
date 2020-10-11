import json
import boto3
import datetime 

s3=boto3.client('s3')

def lambda_handler(event,context):
    date = event['currentIntent']['slots']['date']
    teamA = event['currentIntent']['slots']['TeamA']
    teamB = event['currentIntent']['slots']['TeamB']
    my_date=datetime.datetime.strptime(date,"%Y-%m-%d")
    year=str(my_date.year)
    my_date1=my_date.strftime("%Y-%m-%d")
    bucket='ipldata'
    key='data.json'
    response=s3.get_object(Bucket=bucket,Key=key)
    content = response['Body']
    jsonObject=json.loads(content.read())
    year1=jsonObject[year]
    
   
    for i in year1:
        if(year==i['season'] and my_date1==i['date'] and (teamA==i['team1'] or teamA==i['team2']) and (teamB==i['team1'] or teamB==i['team2'])):
            city=i['city'].replace(" "," ")
            venue=i['venue'].replace(" "," ")
        
            
    
    response={
         "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "PlainText",
              "content": "The match was held in {a},{b}".format(a=city,b=venue)
            }   ,
             
         }
    }
    return response
    return response
