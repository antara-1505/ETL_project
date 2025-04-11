#load.py

import boto3
import json
import config
from datetime import datetime
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def upload_to_s3(data, bucket_name, file_name):
    """
    Uploads data to an S3 bucket.

    :param data: Data to upload (can be a dictionary, list, or string).
    :param bucket_name: The name of the S3 bucket.
    :param file_name: The name of the file to create in the S3 bucket.
    """
    try:
        # Create an S3 client
        s3 = boto3.client('s3',
                          aws_access_key_id=config.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
                          region_name=config.S3_REGION)

        # If the data is a dictionary, convert it to JSON
        if isinstance(data, dict):
            data = json.dumps(data)

        # Upload data to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=data)
        print(f"Data successfully uploaded to S3: {bucket_name}/{file_name}")

    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error: {e}")
        print("Ensure your AWS credentials are properly configured.")
    except Exception as e:
        print(f"An error occurred: {e}")


def load_data_to_s3(data):
    """
    Function to load transformed earthquake data into an S3 bucket.

    :param data: Transformed data to upload to S3.
    """
    # Define S3 bucket and file name
    bucket_name = config.S3_BUCKET_NAME
    # Step 3: Partition the data and generate filename based on today's date
    today_date = datetime.now().strftime('%Y-%m-%d')
    file_name = f"events_{today_date}.json"
    # Upload the data to S3
    upload_to_s3(data, bucket_name, file_name)
