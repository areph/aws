# Serverless Sample Application for CDK

## AWSリソース

- Lambda
- API Gateway

## 各種コマンド

- cdk synth
  - CDKのコードからCloudFormationのテンプレートを生成する
- cdk deploy
  - CloudFormationにCDKで定義したAWSリソースをスタックとしてデプロイする
- cdk diff
  - すでにデプロイ済みのリソースとローカルの差分を出す
- cdk watch
  - 変更を検知して自動でデプロイする
- cdk destroy
  - デプロイしたスタックを削除する

### CDKで作成されたtemplateに対してSAMでローカル実行

```
sam local invoke -t ./cdk.out/ServerlessSampleAppStack.template.json demo-serverless-sample-app-function-for-cdk
```

CDKで作成されたtemplateに対してSAMでローカルのAPIを実行

```
sam local start-api -t ./cdk.out/ServerlessSampleAppStack.template.json
```
