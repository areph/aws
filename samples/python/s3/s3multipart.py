import boto3
from boto3.s3.transfer import TransferConfig

region = 'ap-northeast-1'
bucket_name = '好きなバケット名'
file_name = './50MB.dummy'
key = 'sample/50MB.dummy_sdk.jpg'

# s3クライアント作成
resource = boto3.resource('s3')
bucket = resource.Bucket(bucket_name)
MB = 1024 ** 2
config = TransferConfig(multipart_threshold=5 * MB)

# バケットへマルチパートアップロード
print('S3バケットへアップロード')
# s3.meta.client.upload_file(file_name, bucket_name, key, Config=config)
bucket.upload_file(file_name, key, Config=config)
print(f'./{file_name} -> s3://{bucket_name}/{key}\n')
