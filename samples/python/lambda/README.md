## Lambda サンプル集

### Lambda をマネジメントコンソールで操作

- マネジメントコンソールから Lambda 関数を作成
  - Python 3.9 を選択
  - 実行ロールに DynamoDB への権限が付与されたロールを選択
    - ラボでは `lambdaPollyRole` を使用します
      - どんな権限がついているか確認しておきましょう
- Lambda 関数のコードに [aws/ddbquery.py](https://github.com/areph/aws/blob/main/samples/python/lambda/ddbquery.py) のソースコードを転記
- `Deploy` ボタンでソースコードをデプロイします
- `Test` ボタンで Lambda 関数を実行します
  - 最初は新しいイベントを作成してください
  - イベントJSONはそのままで大丈夫です
  - `保存` して、作成したイベントを指定してテストを実行してみましょう
  - `testuser` のデータが取得できれば成功です
    - DynamoDB の `Notes` テーブルの中身を確認してみましょう
- Lambda 関数のソースコードを見ると `Notes` テーブルを検索する `UserId` がハードコーディングされています
  - `UserId` をイベントで渡せるようにしてみましょう
    - Lambda 関数の `コード` で
      - `UserId = "testuser"` を削除します
      - `# UserId = event["UserId"]` のコメントを外します
        - Python では `#` があるとその先はコメントになります
    - 更新を反映するために `Deploy` します
  - `UserId` をテストイベントで渡してみましょう
    - イベント JSON に `{ "UserId": "testuser" }` を指定して保存、実行してみましょう
    - `UserId` をハードコーディングしなくてもOKになりました
- Lambda 関数のソースコードを見ると `Notes` テーブル名がハードコーディングされています
  - テーブル名を環境変数を参照するようにしてみましょう
    - Lambda 関数の `コード` で
      - `ddbTable = "Notes"` を削除します
      - `# ddbTable = os.environ['TABLE_NAME']` のコメントを外します
    - 更新を反映するために `Deploy` します
  - `設定` → `環境変数` でテーブル名を設定してみましょう
    - `キー` : `TABLE_NAME`
    - `値` : `Notes`
  - テストを実行してみましょう

----
### Lambda へデプロイ

```shell
# 対象ソースをzip化
zip package.zip app.py

# zip化したソースコードをLambdaへアップロードして作成
aws lambda create-function \
--zip-file fileb://package.zip \
--function-name ${LAMBDA_FUNCTION_NAME} \
--handler app.lambda_handler \
--role ${ROLE_NAME}

# zip化したソースコードをLambdaへアップロードして更新
aws lambda update-function-code \
--zip-file fileb://package.zip \
--function-name ${LAMBDA_FUNCTION_NAME}

# 呼び出すhandler名を変更
aws lambda update-function-configuration \
--function-name ${LAMBDA_FUNCTION_NAME} \
--handler ${FILE_NAME}.lambda_handler

# 環境変数を設定
aws lambda update-function-configuration \
--function-name ${LAMBDA_FUNCTION_NAME} \
--environment "Variables={KEY_NAME=VALUE}"
```

ex) hello.py を hello-function 関数として作成する場合
```shell
cd aws/samples/python/lambda/

# 各AWSアカウントIDを設定
ACCOUNT_ID=

# 対象ソースをzip化
zip hello.zip hello.py

# zip化したソースコードをLambdaへアップロードして作成
aws lambda create-function \
--zip-file fileb://hello.zip \
--function-name hello-function \
--runtime python3.9 \
--handler hello.lambda_handler \
--role arn:aws:iam::${ACCOUNT_ID}:role/lambdaPollyRole

# Lambdaを実行するとreponse.txtに出力されます
aws lambda invoke \
--function-name hello-function \
reponse.txt

# 実行ログも見たい場合はlog-type Tailにしてqueryでよしなに見れます
aws lambda invoke \
--function-name hello-function \
--log-type Tail \
reponse.txt \
--query 'LogResult' | tr -d '"' | base64 -d

# 作成後、ソースファイルや各種設定を更新したい場合

## ソースコードを変更したらzip化
zip hello.zip hello.py

## zip化したソースコードをLambdaへアップロードして更新
aws lambda update-function-code \
--zip-file fileb://hello.zip \
--function-name hello-function

## 呼び出すhandler名を変更
aws lambda update-function-configuration \
--function-name hello-function \
--handler hello.lambda_handler
```

ex) ddbquery.py を ddb-search-function 関数として作成する場合
```shell
cd aws/samples/python/lambda/

# 対象ソースをzip化
zip ddbquery.zip ddbquery.py

# zip化したソースコードをLambdaへアップロードして作成
aws lambda create-function \
--zip-file fileb://ddbquery.zip \
--function-name ddb-search-function \
--runtime python3.9 \
--handler ddbquery.lambda_handler \
--role arn:aws:iam::${ACCOUNT_ID}:role/lambdaPollyRole

# 検索条件などハードコーディングしている箇所を外部に切り出して、環境変数やペイロードから読み込ませる

# ソースコードを変更したらzip化
zip ddbquery.zip ddbquery.py

# 環境変数を設定
aws lambda update-function-configuration \
--function-name ddb-search-function \
--environment "Variables={TABLE_NAME=Notes}"

# zip化したソースコードをLambdaへアップロードして更新
aws lambda update-function-code \
--zip-file fileb://ddbquery.zip \
--function-name ddb-search-function

# ペイロードを付けて検索
aws lambda invoke \
--function-name ddb-search-function \
--payload fileb://event.json \
--log-type Tail \
reponse.txt \
--query 'LogResult' | tr -d '"' | base64 -d

# MCからもテスト

```

### Lambda関数実行

そのまま実行
```shell
aws lambda invoke \
--function-name ${LAMBDA_FUNCTION_NAME} reponse.txt
```

ペイロードあり
```shell
aws lambda invoke \
--function-name ${LAMBDA_FUNCTION_NAME} \
--payload fileb://event.json reponse.txt
```
