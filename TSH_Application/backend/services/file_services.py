import logging
import boto3
from botocore.exceptions import ClientError  
import requests
import base64
import os

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_ACCESS_KEY = os.environ.get("SECRET_ACCESS_KEY")
API_KEY = os.environ.get("API_KEY")

s3_client = boto3.client(
    "s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_ACCESS_KEY
)

def fetch_file(object_key):
    try:
        response = s3_client.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": "candidate-uploaded-files",
                "Key": object_key,
            },
            ExpiresIn=60000,
        )
        return response

    except Exception as e:
        logging.error(e)
        return False

def perform_parsing(uploaded):
    url = 'https://cvparser.ai/api/v3/parse'
    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': API_KEY
    }

    with open(uploaded, 'rb') as file:
        encoded_file = base64.b64encode(file.read()).decode('utf-8')

    data = {
        'base64': encoded_file
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()