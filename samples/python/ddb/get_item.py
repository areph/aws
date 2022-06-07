# 依存関係を定義
import boto3
import time

region_name = 'ap-northeast-1'

# dynamodbクライアントを作成
dynamodb = boto3.resource(
    'dynamodb', region_name=region_name, endpoint_url='http://localhost:8000')

# Table情報を取得
table = dynamodb.Table('Demo-Music')

# Tableを操作してデータ取得
res = table.get_item(Key={"Singer": "John", "Title": "XYZ"})

print(res['Item'])
