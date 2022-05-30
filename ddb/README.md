## DynamoDB サンプル集

※：Docker/docker-composeのインストールが必要です

ref: https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html#docker

### DDBローカルを起動

```shell
docker-compose up
```

### Table作成
```shell
aws dynamodb create-table --cli-input-json file://settings/create_table.json  --endpoint-url http://localhost:8000
```

### テストデータ投入
```shell
aws dynamodb batch-write-item --request-items file://settings/input_data.json --endpoint-url http://localhost:8000
```

### データ確認(Scan)

```shell
aws dynamodb scan --table-name Music --endpoint-url http://localhost:8000
```

### PythonのSDKを利用してScan実行

```shell
python python/ddb-scan.py
```

### PartiQL

```shell
python python/partiql.py 
```

### Documentation

[Boto3 Docs for DynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)