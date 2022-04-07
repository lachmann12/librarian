import boto3
import json
from botocore.exceptions import ClientError
import os

config = json.load("secrets/config.json")
bucket_name = "mssm-test"

s3_client = boto3.client(
    's3',
    region_name='us-east-1',
    aws_access_key_id=config.get("aws_id", None),
    aws_secret_access_key=config.get("aws_key", None),
)

def upload_file(file_name, bucket, s3_client, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print(e)
        return False
    return True

upload_file("test/testfile1.txt", bucket_name, s3_client)