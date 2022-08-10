## CDK

### CDKを導入する

Ref:
- https://pages.awscloud.com/rs/112-TZM-766/images/B-3.pdf
- https://github.com/harunobukameda/AWS-CDK-v2

```
npm install -g aws-cdk
exec $SHELL -l
cdk --version

cdk bootstrap aws://<アカウント番号>/<リージョン名>

cdk init app --language typescript
npm run watch # TypeScriptをJavascriptへトランスパイル
cdk synth
cdk deploy
cdk deploy --hotswap # 差分更新-開発用に留める
cdk diff
cdk destroy # Stack削除
```

### CDKで作成されたtemplateに対してSAMでローカル実行

```
sam local invoke -e event.json -t ./cdk.out/xxxxStack.template.json ${FunctionName}
```

CDKで作成されたtemplateに対してSAMでローカルのAPIを実行

```
sam local start-api -t ./cdk.out/xxxxStack.templateson
```
