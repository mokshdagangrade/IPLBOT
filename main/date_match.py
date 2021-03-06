import json
import boto3
import datetime 

s3=boto3.client('s3')

def lambda_handler(event,context):
    date = event['currentIntent']['slots']['date']
    #year = event['currentIntent']['slots']['year']
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
        if(year==i['season'] and my_date1==i['date']):
            t1=i['team1'].replace(" "," ")
            t2=i['team2'].replace(" "," ")
        
            
    
    response={
         "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "PlainText",
              "content": "The teams are {a} and {b}".format(a=t1,b=t2)
            }   ,
             
         }
    }
    return response
