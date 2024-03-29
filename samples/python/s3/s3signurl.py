# 依存関係を定義
import boto3

region = 'ap-northeast-1'
bucket_name = '好きなバケット名'
key = 'sample/lovot.jpg'

# s3クライアント作成
s3 = boto3.client('s3', region_name=region)

# 署名付きURLの発行
print('署名付きURLの発行 (5分)')
res = s3.generate_presigned_url(
    'get_object',
    Params={
        'Bucket': bucket_name,
        'Key': key
    },
    ExpiresIn=60 * 5
)
print(f'{res}\n')
