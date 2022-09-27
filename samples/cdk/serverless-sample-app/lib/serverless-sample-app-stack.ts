import {
  App, Stack, StackProps, DefaultStackSynthesizer,
  aws_lambda as lambda,
  aws_apigateway as apigw,
} from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class ServerlessSampleAppStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Lambda
    const helloFunction = new lambda.Function(this, 'ServerlessSampleFunction', {
      functionName: 'demo-serverless-sample-app-function-for-cdk',
      runtime: lambda.Runtime.NODEJS_16_X,
      code: lambda.Code.fromAsset('src/lambda'),
      handler: 'index.handler',
      description: 'CDKで作成したサンプルLambda関数'
    })

    // APIGWを作成してLambdaを統合
    const api = new apigw.LambdaRestApi(this, 'ServerlessSampleAPI', {
      restApiName: 'demo-serverless-sample-app-api-for-cdk',
      handler: helloFunction,
      cloudWatchRole: false,
      deployOptions: {
        tracingEnabled: true
      },
      description: 'CDKで作成したサンプルAPIGW1',
      proxy: false
    })
    api.root.addMethod('GET')
  }
}
