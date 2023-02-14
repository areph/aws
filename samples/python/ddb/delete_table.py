# 依存関係を定義
import boto3
import time

# dynamodbクライアントを作成
dynamodb = boto3.resource('dynamodb')

print(f'テーブル削除開始：{time.gmtime()}')

# Table情報を取得
table = dynamodb.Table('Demo-Music')
# テーブル削除
table.delete()

print(f'テーブル削除終了：{time.gmtime()}')
