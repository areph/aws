## DynamoDB サンプル集

※：Docker/docker-composeのインストールが必要です

ref: https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html#docker

### DDBローカルを起動

```shell
docker-compose up
```

### テーブル作成

```shell
python create_table.py
```

### Scanしてデータを全取得

```shell
python scan.py
```

### PartiQL

```shell
python partiql.py 
```

### Documentation

[Boto3 Docs for DynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)