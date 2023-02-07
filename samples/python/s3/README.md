## SDK(Python)を使ってS3を操作する

### 準備

```
git clone https://github.com/areph/aws.git
cd ~/environment/aws/samples/python/s3
```
### リージョンを取得

```shell
REGION=`aws configure get region`
echo $REGION
```

### ソースコードの確認

ソースコードに埋め込まれているリージョンは上記shellで出力されたリージョンに変更してください

### boto3 API リファレンスの調べ方

英語で読みづらいかもしれませんが、翻訳をしたりコード例から当たりをつけていきながらコーディングしていきましょう
[Boto3 documentation — Boto3 Docs 1.26.65 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

例えばS3でバケットを作成したい場合…
- S3のリファレンスを見つける
  - [S3 — Boto3 Docs 1.26.65 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
- clientの作成方法を確認する
  - `client = boto3.client('s3')`
  - [S3 — Boto3 Docs 1.26.65 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#client)
- バケットが作成できそうな関数を探す
  - バケット作成…create bucketあたりかな？
  - [S3 — Boto3 Docs 1.26.65 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.create_bucket)
- ドキュメントを読みながら必要な引数を設定する
  - `Request Syntax` や `Examples` で記述例をざっくり眺めると参考になるのでおすすめです
- 同じように `やりたいこと` から逆引きしていくとドキュメントから探しやすいです
  - 例えば、Webサイトホスティングを設定するには… `website` `hosting` などをキーに探すなど

### S3バケットを作成して完了するまで待つ

`client API` でバケットを作成するコーディングをします

```
python s3bucket.py
```

出力されたランダムのバケット名をコピーしておきます
また、マネジメントコンソール上でもバケットが作成されたか確認します

### オブジェクトをアップロードする

s3put.py の下記を変更します
- バケット名
- リージョン

今度は `resource API` を使ってコーディングしてみます。できることはほとんど同じですが、より抽象度が高くAPIを操作できます

[S3 — Boto3 Docs 1.26.65 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#bucket)

```
python s3put.py
```

マネジメントコンソール上でもオブジェクトがアップロードされたか確認します

### オブジェクトをダウンロードする

s3get.py の下記を変更します
- バケット名
- リージョン

今回も `resource API` を使ってコーディングします。

```
python s3get.py
```

### S3 Select

data/sample.csvの中身を確認します
s3select.py の下記を変更します
- バケット名
- リージョン

sample.csvをアップロードしたあと、 `select_object_content` で S3 Select を行います。
このとき、 S3 Select は `resource API` にないため、 `client API` を使って操作します

[S3 — Boto3 Docs 1.26.65 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.select_object_content)

```
python s3select.py
```

### 署名付きURL

s3signurl.py の下記を変更します
- バケット名
- リージョン

一時的にアクセス可能な署名付きURLを発行します

```
python s3signurl.py
```

### マルチパートアップロード

```
dd if=/dev/zero of=50MB.dummy bs=1M count=50
python s3multipart.py
```
