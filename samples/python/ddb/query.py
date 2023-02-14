# 依存関係を定義
import boto3
from boto3.dynamodb.conditions import Key

# dynamodbクライアントを作成
dynamodb = boto3.resource('dynamodb')
# dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000') for Docker

# Table情報を取得
table = dynamodb.Table('Demo-Music')

# Tableを操作してデータ取得(クエリ)
print('---ex) Singer conditions---')
res = table.query(KeyConditionExpression=Key('Singer').eq('John'))
items = res['Items']
print(items)

print('---ex) Singer conditions with SortKey---')
res = table.query(
    KeyConditionExpression=Key('Singer').eq('John') & Key('Title').eq('ABC'))
items = res['Items']
print(items)
