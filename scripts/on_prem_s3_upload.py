import boto3
import os

import configparser
config = configparser.ConfigParser()
config.read_file(open('../configurations/annotation.config'))

# AWS credentials
AWS_ACCESS_KEY_ID = config.get('AWS', 'ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = config.get('AWS', 'SECRET_KEY')
AWS_REGION_NAME = config.get('AWS', 'REGION')

# S3 bucket information
BUCKET_NAME = config.get('AWS', 'LABELED_IMAGE_BUCKET_NAME')

# Function to upload files to S3
def upload_to_s3(file_path, bucket_name, folder_name=None):
    # Connect to S3
    s3 = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=AWS_REGION_NAME)
    
    # Prepare the S3 key
    s3_key = os.path.basename(file_path)
    
    # Upload file to S3
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"File uploaded successfully to S3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")


# Local directory containing image files
local_directory = '../data/to_Send/'

# List all image files in the directory
image_files = [f for f in os.listdir(local_directory) if f.endswith(('.jpg', '.jpeg', '.png'))]


# Upload each image file to S3
for file_name in image_files:
    file_path = os.path.join(local_directory, file_name)
    upload_to_s3(file_path, BUCKET_NAME)