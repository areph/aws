## SAMサンプルコマンド

ref:https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html

### SAMプロジェクト作成

```shell
sam init
```

### SAMでビルド

```shell
sam build
```

コンテナを使ってビルドすれば環境にランタイムが無くても平気です

```shell
sam build --use-container
```

### SAMでローカル実行

```shell
sam local invoke
```

### SAMでローカルでAPI実行

```shell
sam local start-api
```

### SAMでデプロイ

```shell
sam deploy --guided
```

### 変更を検知して自動デプロイ

```shell
sam sync --stack-name ${STACK_NAME} --region ap-northeast-1 --watch
```

Lambda関数のコードを修正して保存すると自動でデプロイします

### SAMで作成したスタックを削除

```shell
sam delete
```

```shell
sam delete --region ap-northeast-1
```
