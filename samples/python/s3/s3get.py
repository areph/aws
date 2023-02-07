# 依存関係を定義
import boto3

region = 'ap-northeast-1'
bucket_name = '好きなバケット名'
file_name = 'download-lovot.jpg'
key = 'sample/lovot.jpg'

# s3クライアント作成
resource = boto3.resource('s3', region_name=region)
bucket = resource.Bucket(bucket_name)

# S3からオブジェクトをダウンロード
print('S3からダウンロード(s3:GetObject)')
bucket.download_file(key, file_name)
print(f's3://{bucket_name}/{key} -> ./{file_name}\n')
