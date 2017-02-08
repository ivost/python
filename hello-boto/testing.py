import boto3

print("Hello1")

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)
