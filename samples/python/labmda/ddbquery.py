import boto3
import os
from boto3.dynamodb.conditions import Key

dynamoDBResource = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    # Log debug information
    print(event)
    
#    UserId = event["UserId"]
    UserId = "testuser"
    # ddbTable = os.environ['TABLE_NAME']
    ddbTable = "Notes"
    
    table = dynamoDBResource.Table(ddbTable)
    records = table.query(KeyConditionExpression=Key('UserId').eq(UserId))
    
    return records
