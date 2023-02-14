import json
import boto3

tableName = 'Demo-Music'
pageSize = 3

client = boto3.client('dynamodb')

paginator = client.get_paginator('scan')

page_iterator = paginator.paginate(
    TableName=tableName,
    PaginationConfig={
    'PageSize': pageSize
    })

pageNumber = 0
for page in page_iterator:
    if page["Count"] > 0:
        pageNumber += 1
        print("Starting page " + str(pageNumber))
        for item in page['Items']:
            print(item)
        print("End of page " + str(pageNumber) + "\n")    
