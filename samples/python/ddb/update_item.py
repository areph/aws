# 依存関係を定義
import boto3
import time

# dynamodbクライアントを作成
dynamodb = boto3.resource('dynamodb')

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
