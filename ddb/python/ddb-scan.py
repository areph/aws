import boto3


def scan():
    dynamodb = boto3.resource('dynamodb',
                              endpoint_url='http://localhost:8000',
                              region_name='ap-northeast-1',
                              aws_access_key_id="xxx",
                              aws_secret_access_key='xxx'
                              )
    table = dynamodb.Table('Music')
    res = table.scan()
    for item in res['Items']:
        print(item)


if __name__ == '__main__':
    scan()
