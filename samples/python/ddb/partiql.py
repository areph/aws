import boto3

client = boto3.client('dynamodb')
res = client.execute_statement(
    Statement='SELECT * FROM "Demo-Music" WHERE Singer IN [\'John\', \'Marry\']',
    ReturnConsumedCapacity='TOTAL'
    )
print(res)
print('==========================')
for item in res['Items']:
    print(item)
