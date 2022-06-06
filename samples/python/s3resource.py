import boto3

# セッションとして認証情報を取得
session = boto3.session.Session()

# セッションからリージョンを取得
current_region = session.region_name
print(current_region)

# セッションから高レベルAPIを操作
resource = session.resource('s3')

# バケットを作成する方法に注目
bucket = resource.Bucket('${作成したいバケット名}')
bucket.create(
    CreateBucketConfiguration={
        'LocationConstraint': current_region
    })
