## Lambdaサンプル集

### Lambdaへデプロイ

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
# 対象ソースをzip化
zip hello.zip hello.py

# zip化したソースコードをLambdaへアップロードして作成
aws lambda create-function \
--zip-file fileb://hello.zip \
--function-name hello-function \
--runtime python3.9 \
--handler hello.lambda_handler \
--role arn:aws:iam::${ACCOUNT_ID}:role/lambdaPollyRole

or

# zip化したソースコードをLambdaへアップロードして更新
aws lambda update-function-code \
--zip-file fileb://hello.zip \
--function-name hello-function

# 呼び出すhandler名を変更
aws lambda update-function-configuration \
--function-name hello-function \
--handler hello.lambda_handler
```

ex) ddbquery.py を ddb-search-function 関数として作成する場合
```shell
# 対象ソースをzip化
zip ddbquery.zip ddbquery.py

# zip化したソースコードをLambdaへアップロードして作成
aws lambda create-function \
--zip-file fileb://ddbquery.zip \
--function-name ddb-search-function \
--runtime python3.9 \
--handler ddbquery.lambda_handler \
--role arn:aws:iam::536655976692:role/lambdaPollyRole

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
--payload fileb://event.json reponse.txt

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
