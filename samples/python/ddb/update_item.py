# 依存関係を定義
import boto3
import time

region_name = 'ap-northeast-1'

# dynamodbクライアントを作成
dynamodb = boto3.resource('dynamodb', region_name=region_name)
# dynamodb = boto3.resource(
#     'dynamodb', region_name=region_name, endpoint_url='http://localhost:8000') for Docker

# Table情報を取得
table = dynamodb.Table('Demo-Music')

# 条件付き更新
date = '20220630'
table.update_item(
    Key={"Singer": "John", "Title": "XYZ"},
    UpdateExpression='set #attr = :date',
    # ReleaseDateが指定した日より過去の場合、指定日で更新
    ConditionExpression="#attr < :date",
    ExpressionAttributeNames={
        '#attr': 'ReleaseDate',
    },
    ExpressionAttributeValues={
        ':date': date,
    },
    ReturnValues='UPDATED_NEW'
)
