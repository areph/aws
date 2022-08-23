## SDK(Python)を使ってS3を操作する

### 準備

```
cd ~/environment/aws/samples/python/s3
```

### S3バケットを作成して完了するまで待つ

```
python s3bucket.py
```

作成されたバケット名をコピーしておく

### オブジェクトをアップロードする

s3put.py のバケット名を変更する

```
python s3put.py
```

### オブジェクトをダウンロードする

s3get.py のバケット名を変更する

```
python s3get.py
```

### S3 Select

data/sample.csvの中身を確認する
s3select.py のバケット名を変更する

```
python s3select.py
```

### マルチパートアップロード

```
dd if=/dev/zero of=50MB.dummy bs=1M count=50
python s3multipart.py
```

### 署名付きURL

s3signurl.py のバケット名を変更する

```
python s3signurl.py
```
