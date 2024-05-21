import os
import json
import boto3
from kafka import KafkaProducer
from time import sleep

# Kafka broker's IP address and port
bootstrap_servers = '3.144.237.39:9092'

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        file_name = os.path.basename(object_key)

        # Download the file from S3
        download_path = f'/tmp/{file_name}'
        
        try:
            s3.download_file(bucket_name, object_key, download_path)
            print(f"Downloaded {object_key} from {bucket_name} to {download_path}")
        except Exception as e:
            print(f"Error downloading file from S3: {e}")
            raise

        # Read the file and send it to Kafka
        with open(download_path, 'rb') as file:
            image_data = file.read()
            producer.send('demo_testing2', value=image_data)
            producer.flush()
            print("Image sent successfully to Kafka topic")
            sleep(1)  # Optional: control the rate of sending messages

    return {
        'statusCode': 200,
        'body': json.dumps('Image sent to Kafka topic successfully!')
    }
