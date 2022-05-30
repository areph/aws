from email.mime import image
import boto3
import json


def partiql():
    client = boto3.client('dynamodb',
                          endpoint_url='http://localhost:8000',
                          region_name='ap-northeast-1')
    res = client.execute_statement(
        Statement="SELECT * FROM Music WHERE MusicID IN ['1', '2', '3']")
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    partiql()
