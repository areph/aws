# 依存関係を定義
import boto3
import time

# dynamodbクライアントを作成
dynamodb = boto3.resource('dynamodb')

# Table情報を取得
table = dynamodb.Table('Demo-Music')

# Tableを操作してデータ取得
res = table.get_item(Key={"Singer": "John", "Title": "XYZ"})

print(res['Item'])
