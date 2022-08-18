## DynamoDB サンプル集

## ローカルにコンテナを立ててテスト的にDynamoDBを操作する

実態としてDynamoDBを作成してしまうと料金がかかってしまったり各々で開発するのに不便なため、ローカル環境にDynamoDBを用意して好きに操作できる環境をDockerで構築します

docker-compose.yml に DynamoDBのイメージを記述しコンテナを起動した後、各種コマンドに `--endpoint-url http://localhost:8000` を付けて実行します

※：Docker/docker-composeのインストールが必要です

- ref: https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html#docker
- ref: https://matsuand.github.io/docs.docker.jp.onthefly/compose/install/

### Cloud9 で試す

- Cloud9 を起動
- すでにDockerはインストール済みのため、docker-composeをインストール

```shell
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.4.1/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
docker compose version
```
### DDBローカルを起動

```shell
docker-compose up -d
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
aws dynamodb scan --table-name Demo-Music --endpoint-url http://localhost:8000  --return-consumed-capacity TOTAL
```

### データ検索(Query)
```shell
aws dynamodb query --key-condition-expression "Singer = :v1" --expression-attribute-values '{":v1": {"S": "John"}}' --table-name Demo-Music --endpoint-url http://localhost:8000 --return-consumed-capacity TOTAL 
```

Countのみ
```shell
aws dynamodb query --select COUNT --key-condition-expression "Singer = :v1" --expression-attribute-values '{":v1": {"S": "John"}}' --table-name Demo-Music --endpoint-url http://localhost:8000
```

### データ取得(GetItem:結果整合性)

```shell
aws dynamodb get-item --table-name Demo-Music --endpoint-url http://localhost:8000 --key '{"Singer": {"S": "John"}, "Title": {"S": "XYZ"}}' --return-consumed-capacity TOTAL
```

### データ取得(GetItem:強い整合性)

```shell
aws dynamodb get-item --table-name Demo-Music --endpoint-url http://localhost:8000 --key '{"Singer": {"S": "John"}, "Title": {"S": "XYZ"}}' --consistent-read --return-consumed-capacity TOTAL
```

### データ追加・更新(UpdateItem)

```shell
aws dynamodb update-item --table-name Demo-Music --endpoint-url http://localhost:8000 --key '{"Singer": {"S": "Yan"}, "Title": {"S": "Super"}}'
```

### データ削除(DeleteItem)

```shell
aws dynamodb delete-item --table-name Demo-Music --endpoint-url http://localhost:8000 --key '{"Singer": {"S": "Yan"}, "Title": {"S": "Super"}}'
```

### Table削除
```shell
aws dynamodb delete-table --table-name Demo-Music --endpoint-url http://localhost:8000
```
