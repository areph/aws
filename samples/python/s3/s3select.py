# 依存関係を定義
import boto3

region = 'ap-northeast-1'
bucket_name = 'lab-bucket-0358-2851-52-test'
file_name = '../../data/sample.csv'
key = 'sample.csv'

# s3クライアント作成
resource = boto3.resource('s3', region_name=region)
bucket = resource.Bucket(bucket_name)

# バケットへアップロード
print('S3バケットへアップロード')
bucket.upload_file(file_name, key)
print(f'./{file_name} -> s3://{bucket_name}/{key}\n')

s3 = boto3.client('s3')
res = s3.select_object_content(
    Bucket=bucket_name,
    Key=key,
    ExpressionType='SQL',
    Expression="SELECT first_name FROM s3object s WHERE s.\"city\" = 'New York'",
    InputSerialization={'CSV': {"FileHeaderInfo": "Use"}},
    OutputSerialization={'CSV': {}}
)

for event in res['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)
    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print(f'S3 SELECT終了：{statsDetails}')
