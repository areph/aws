import json
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

translate = boto3.client('translate')

def lambda_handler(event, context):
    logger.info(event)

    # 翻訳処理呼び出し
    input_text = event['queryStringParameters']['input_text']
    response = translate.translate_text(
        Text=input_text,
        SourceLanguageCode='ja',
        TargetLanguageCode='en',
    )
    # 翻訳結果を取得
    output_text = response.get('TranslatedText')

    return {
        'statusCode': 200,
        'body': json.dumps({
            'output_text': output_text
        }),
        'isBase64Encoded': False,
        'headers': {}
    }
