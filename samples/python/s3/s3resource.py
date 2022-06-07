# 依存関係を定義
import boto3
import uuid

# セッションとして認証情報を取得
session = boto3.session.Session()

# セッションからリージョンを取得
current_region = session.region_name
print(current_region)

# セッションから高レベルAPIを操作
resource = session.resource('s3')

# セッションからではなくboto3からclientを生成することも可能
#resource = boto3.resource('s3', region_name=current_region)

bucket_name = f'dev-bucket-{uuid.uuid4()}'
print(f'作成するバケット名: {bucket_name}')

# バケットを作成する方法に注目
bucket = resource.Bucket(bucket_name)
bucket.create(
    CreateBucketConfiguration={
        'LocationConstraint': current_region
    })
