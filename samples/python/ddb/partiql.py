from email.mime import image
import boto3
import json


def partiql():
    client = boto3.client('dynamodb')
    res = client.execute_statement(
        Statement='SELECT * FROM "Demo-Music" WHERE Singer IN [\'John\', \'Marry\']')
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    partiql()
