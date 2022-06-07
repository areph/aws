# 依存関係を定義
import boto3
import time

region_name = 'ap-northeast-1'

# dynamodbクライアントを作成
dynamodb = boto3.resource(
    'dynamodb', region_name=region_name, endpoint_url='http://localhost:8000')

print(f'テーブル削除開始：{time.gmtime()}')

# Table情報を取得
table = dynamodb.Table('Demo-Music')
# テーブル削除
table.delete()

print(f'テーブル作成終了：{time.gmtime()}')
