import boto3
from boto3.dynamodb.conditions import Key


def scan():
    print('---ex) Music Table Scan---')
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

    print('---ex) MusicID conditions---')
    res = table.query(KeyConditionExpression=Key('MusicID').eq('2'))

    items = res['Items']
    print(items)

    print('---ex) MusicID conditions with SortKey---')
    res = table.query(KeyConditionExpression=Key(
        'MusicID').eq('1') & Key('ReleaseDate').eq('20220608'))
    items = res['Items']
    print(items)


if __name__ == '__main__':
    scan()
