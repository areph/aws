import json
import os
import boto3

sqs = boto3.resource('sqs')
sns = boto3.resource('sns')
from aws_xray_sdk.core import patch
patch(['boto3'])

qname = os.getenv('QUEUE_NAME')
snsname = os.getenv('TOPIC_ARN')

def handler(event, context):
    print(event)
    query = event['queryStringParameters'] or {'message': '[Default Message]'}
    print({'Query': query, 'qname': qname, 'snsname': snsname})

    # SQS
    queue = sqs.get_queue_by_name(QueueName=qname)

    msg_num = 10
    msg_list = [{'Id' : '{}'.format(i + 1), 'MessageBody' : '{} - {}'.format(query['message'], i + 1)} for i in range(msg_num)]
    response = queue.send_messages(Entries=msg_list)
    print(response)

    # SNS
    topic = sns.Topic(snsname)
    response = topic.publish(Message='test')
    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }
