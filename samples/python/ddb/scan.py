import boto3

def scan():
    print('---ex) Music Table Scan---')
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Demo-Music')
    res = table.scan()
    for item in res['Items']:
        print(item)

if __name__ == '__main__':
    scan()
