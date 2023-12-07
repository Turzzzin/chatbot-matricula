import boto3

s3 = boto3.client('s3')
lex = boto3.client('lexv2-runtime')
transcribe = boto3.client('transcribe')