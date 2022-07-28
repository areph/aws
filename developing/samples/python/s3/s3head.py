# 依存関係を定義
import boto3

region = 'ap-northeast-1'
bucket_name = '好きなバケット名'
file_name = '../../data/lavot.jpg'
key = 'sample/lavot.jpg'

# s3クライアント作成
client = boto3.client('s3', region_name=region)

# オブジェクトの情報を取得
print('S3バケットからオブジェクト情報取得(s3:HeadObject)')
res = client.head_object(Bucket=bucket_name, Key=key)
print(f'{res}\n')
