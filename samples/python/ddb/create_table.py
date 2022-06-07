# 依存関係を定義
import boto3
import time

region_name = 'ap-northeast-1'

# dynamodbクライアントを作成
dynamodb = boto3.resource(
    'dynamodb', region_name=region_name, endpoint_url='http://localhost:8000')

print(f'テーブル作成開始：{time.gmtime()}')

# dynamodbクライアントを使ってテーブル作成
table = dynamodb.create_table(
    TableName='Demo-Music',
    KeySchema=[
        {'AttributeName': 'Singer', 'KeyType': 'HASH'},  # Partition key
        {'AttributeName': 'Title', 'KeyType': 'RANGE'},  # Sort key
    ],
    AttributeDefinitions=[
        {'AttributeName': 'Singer', 'AttributeType': 'S'},
        {'AttributeName': 'Title', 'AttributeType': 'S'}
    ],
    ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
)
table.wait_until_exists()

print(f'テーブル作成終了：{time.gmtime()}')
