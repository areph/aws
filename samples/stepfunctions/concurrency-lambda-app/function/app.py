import boto3
import json
import time
from aws_xray_sdk.core import patch
patch(['boto3'])

def lambda_handler(event, context):
    print(event)
    # flg = sleepの場合、10秒sleepする
    flgvalue = event['flg']
    print(flgvalue)
    if flgvalue=='sleep':
        time.sleep(10)

    # ダミーのデータを返す。
    res =  [{'customerId' : '100', 'customerName': 'Allen' },{'customerId' : '200', 'customerName': 'Bob' },{'customerId' : '300', 'customerName': 'Carlos' }];
    return {
        'statusCode': 200,
        'body': json.dumps(res),
        'isBase64Encoded': False,
        'headers': { }
    }