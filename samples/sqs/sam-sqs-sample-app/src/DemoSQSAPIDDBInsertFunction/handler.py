import os
import boto3
import datetime

ddb = boto3.resource('dynamodb')
from aws_xray_sdk.core import patch
patch(['boto3'])

table_name = os.getenv('TABLE_NAME')
table = ddb.Table(table_name)
def handler(event, context):
    print(event)

    now = str(datetime.datetime.now())
    for record in event['Records']:
        response = table.put_item(
            Item={
                'messageId': record['messageId'],
                'datetime': now,
                'message': record['body']
            }
        )

    return {}