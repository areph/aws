## DynamoDB サンプル集


### Table作成
```shell
aws dynamodb create-table \
--cli-input-json file://settings/create_table.json
```

### テストデータ投入
```shell
aws dynamodb put-item \
--table-name Demo-Music \
--item '{"Singer": {"S": "John"}, "Title": {"S": "ABC"}}'

aws dynamodb put-item \
--table-name Demo-Music \
--item '{"Singer": {"S": "Marry"}, "Title": {"S": "Hi"}}'

aws dynamodb put-item \
--table-name Demo-Music \
--item '{"Singer": {"S": "Bob"}, "Title": {"S": "Hello"}, "ReleaseDate": {"S": "20220610"}}'

aws dynamodb put-item \
--table-name Demo-Music \
--item '{"Singer": {"S": "John"}, "Title": {"S": "XYZ"}, "ReleaseDate": {"S": "20220610"}}'

```

### データ確認(Scan)

```shell
aws dynamodb scan \
--table-name Demo-Music \
--return-consumed-capacity TOTAL
```

### データ検索(Query)
```shell
aws dynamodb query \
--table-name Demo-Music \
--key-condition-expression "Singer = :v1" \
--expression-attribute-values '{":v1": {"S": "John"}}' \
--return-consumed-capacity TOTAL 
```

Countのみ
```shell
aws dynamodb query \
--select COUNT \
--table-name Demo-Music \
--key-condition-expression "Singer = :v1" \
--expression-attribute-values '{":v1": {"S": "John"}}' \
--return-consumed-capacity TOTAL 
```

### データ取得(GetItem:結果整合性)

```shell
aws dynamodb get-item --table-name Demo-Music \
--key '{"Singer": {"S": "John"}, "Title": {"S": "XYZ"}}' \
--return-consumed-capacity TOTAL
```

### データ取得(GetItem:強い整合性)

```shell
aws dynamodb get-item --table-name Demo-Music \
--key '{"Singer": {"S": "John"}, "Title": {"S": "XYZ"}}' \
--consistent-read \
--return-consumed-capacity TOTAL
```

### データ追加・更新(UpdateItem)

同一のパーティションキー＆ソートキーが存在しない場合は追加
```shell
aws dynamodb update-item --table-name Demo-Music \
--key '{"Singer": {"S": "Yan"}, "Title": {"S": "Super"}}' \
--return-values ALL_NEW
```

```shell
aws dynamodb update-item --table-name Demo-Music \
--key '{"Singer": {"S": "Yan"}, "Title": {"S": "Great"}}' \
--update-expression "SET ReleaseDate = :newval" \
--expression-attribute-values '{":newval":{"S": "20221231"}}' \
--return-values ALL_NEW
```

同一のパーティションキー＆ソートキーが存在する場合は更新
```shell
aws dynamodb update-item --table-name Demo-Music \
--key '{"Singer": {"S": "Bob"}, "Title": {"S": "Hello"}}' \
--update-expression "SET ReleaseDate = :newval" \
--expression-attribute-values '{":newval":{"S": "20220101"}}' \
--return-values ALL_NEW
```

### データ削除(DeleteItem)

```shell
aws dynamodb delete-item \
--table-name Demo-Music \
--key '{"Singer": {"S": "Yan"}, "Title": {"S": "Super"}}'
```

### Table削除
```shell
aws dynamodb delete-table \
--table-name Demo-Music
```
