## DynamoDB サンプル集

### 準備

- Cloud9 を起動します
- サンプルコードを git clone(すでにcloneされている場合は省略してください)

```shell
cd ~/environment
git clone https://github.com/areph/aws.git
```

- Python のサンプルコードディレクトリへ移動します

```shell
cd ~/environment/aws/samples/python/ddb
```

### テーブル作成

```shell
python create_table.py
```

下記のエラーが発生した場合は

```
Traceback (most recent call last):
  File "create_table.py", line 2, in <module>
    import boto3
ModuleNotFoundError: No module named 'boto3'
```

こちらのコマンドを実行して boto3 をインストールしてください

```shell
python3 -m pip install --user boto3
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