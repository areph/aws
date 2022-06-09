## DynamoDB サンプル集

### テーブル作成

```shell
python create_table.py
```

### データ登録

```shell
python put_item.py
```

### GetItemで1件取得

```shell
python get_item.py
```

### Scanしてデータを全取得

```shell
python scan.py
```

### Queryで条件を指定してデータを取得

```shell
python query.py
```

### PartiQLで検索

```shell
python partiql.py 
```

### Scanしてデータをページングで取得

```shell
python pagenate.py
```

### データ追加・更新・条件付き更新

```shell
python update_item.py
```


### テーブル削除

```shell
python delete_table.py
```

### Documentation

[Boto3 Docs for DynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)