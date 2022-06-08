# 依存関係を定義
from curses import keyname
import boto3
import time

region_name = 'ap-northeast-1'

# dynamodbクライアントを作成
dynamodb = boto3.resource('dynamodb', region_name=region_name)
# dynamodb = boto3.resource(
#     'dynamodb', region_name=region_name, endpoint_url='http://localhost:8000') for Docker

# Table情報を取得
table = dynamodb.Table('Demo-Music')

# Tableを操作してデータ取得(クエリ)
res = table.query(
    KeyConditionExpression="Singer = :v1",
    ExpressionAttributeValues={":v1": "John"})

print(res['Items'])
