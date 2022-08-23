# 依存関係を定義
import boto3
import uuid

# セッションとして認証情報を取得
session = boto3.session.Session()

# セッションからリージョンを取得
current_region = session.region_name
print(current_region)

# セッションから低レベルAPIを操作
client = session.client('s3')

# セッションからではなくboto3からclientを生成することも可能
#client = boto3.client('s3', region_name=current_region)

bucket_name = f'dev-bucket-{uuid.uuid4()}'
print(f'作成するバケット名: {bucket_name}')

# バケットを作成する方法に注目
client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': current_region
    }
)
