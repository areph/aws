import json
import os
import boto3

from aws_xray_sdk.core import patch
patch(['boto3'])

def handler(event, context):
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }
