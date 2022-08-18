# 依存関係を定義
import boto3
import uuid
import time

region = 'ap-northeast-1'
bucket_name = f'dev-bucket-{uuid.uuid4()}'
print(f'作成するバケット名: {bucket_name}')

# s3クライアント作成
s3client = boto3.client('s3')

# バケット作成
s3client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)

print(f'バケット作成開始：{time.gmtime()}')

# バケットが作成されるまで待つ
waiter = s3client.get_waiter('bucket_exists')
waiter.wait(Bucket=bucket_name)

print(f'バケット作成終了：{time.gmtime()}')

# バケットの情報を取得
print('s3:HeadBucket')
res = s3client.head_bucket(Bucket=bucket_name)
print(f'{res}\n')
