import boto3

# セッションとして認証情報を取得
session = boto3.session.Session()

# セッションからリージョンを取得
current_region = session.region_name

# セッションから低レベルAPIを操作
client = session.client('s3')

# バケットを作成する方法に注目
client.create_bucket(
    Bucket='${作成したいバケット名}',
    CreateBucketConfiguration={
        'LocationConstraint': current_region
    }
)
