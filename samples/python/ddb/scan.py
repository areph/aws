import boto3
from boto3.dynamodb.conditions import Key


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

    print('---ex) Singer conditions---')
    res = table.query(KeyConditionExpression=Key('Singer').eq('John'))

    items = res['Items']
    print(items)

    print('---ex) Singer conditions with SortKey---')
    res = table.query(KeyConditionExpression=Key(
        'Singer').eq('John') & Key('Title').eq('ABC'))
    items = res['Items']
    print(items)


if __name__ == '__main__':
    scan()
