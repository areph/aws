# Serverless Sample Application for SAM

## AWSリソース

- Lambda
- API Gateway

## 各種コマンド

- sam build
  - SAMテンプレートに問題がないかチェック
- sam local invoke
  - ローカルでSAMのLambda関数を実行する
- sam local start-api
  - ローカルでSAMのAPI Gateway(みたいなもの)を実行する
- sam deploy --guided
  - SAMの内容をAWSへデプロイする
- sam sync --stack-name ${STACK_NAME} --region ap-northeast-1 --watch
  - 変更を検知して自動デプロイする
  - Lambda関数のコードを修正して保存すると自動でデプロイします
- sam delete --region ap-northeast-1
  - スタックを削除する