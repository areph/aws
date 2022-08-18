import boto3

def scan():
    print('---ex) Music Table Scan---')
    dynamodb = boto3.resource(
        'dynamodb',
        region_name='ap-northeast-1'
    )
    # dynamodb = boto3.resource( for Docker
    #     'dynamodb',
    #     endpoint_url='http://localhost:8000',
    #     region_name='ap-northeast-1',
    #     aws_access_key_id="xxx",
    #     aws_secret_access_key='xxx'
    # )

    table = dynamodb.Table('Demo-Music')
    res = table.scan()
    for item in res['Items']:
        print(item)

if __name__ == '__main__':
    scan()
