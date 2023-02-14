# 依存関係を定義
import boto3
import time

# dynamodbクライアントを作成
dynamodb = boto3.resource('dynamodb')

# Table情報を取得
table = dynamodb.Table('Demo-Music')

# Tableを操作してデータ取得(結果整合性)
res = table.get_item(Key={"Singer": "John", "Title": "XYZ"}, ConsistentRead=False, ReturnConsumedCapacity='TOTAL')

print('GetItem(結果整合性)')
print(res['Item'])
print('-----------------')
print(res)

print()
print('==============================')
print()

# Tableを操作してデータ取得(強い整合性)
res = table.get_item(Key={"Singer": "John", "Title": "XYZ"}, ConsistentRead=True, ReturnConsumedCapacity='TOTAL')

print('GetItem(強い整合性)')
print(res['Item'])
print('-----------------')
print(res)
