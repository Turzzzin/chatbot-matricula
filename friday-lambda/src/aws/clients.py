import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')
rekognition = boto3.client('rekognition', region_name='us-east-1')
s3 = boto3.client('s3')