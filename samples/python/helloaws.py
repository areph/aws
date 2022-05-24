import boto3

s3 = boto3.resource('s3')

buffer = ""
for bucket in s3.buckets.all():
    buffer += bucket.creation_date.strftime("%Y %m %d") + ", " + bucket.name + "\n"

print(buffer)