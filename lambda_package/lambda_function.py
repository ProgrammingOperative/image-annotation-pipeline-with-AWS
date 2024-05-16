import json
import os
import boto3
from kafka import KafkaProducer

# Kafka broker's IP address and port
bootstrap_servers = '3.147.45.97:9092'

# Kafka topic to produce to
topic = 'demo_testing2'

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

def lambda_handler(event, context):
    # Get the uploaded file details
    s3 = boto3.client('s3')
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        file_name = os.path.basename(object_key)

        # Download the file from S3
        download_path = '/tmp/{}'.format(file_name)
        s3.download_file(bucket_name, object_key, download_path)

        # Read the file and send it to Kafka
        with open(download_path, 'rb') as file:
            producer.send(topic, file.read())
    
    return {
        'statusCode': 200,
        'body': json.dumps('Image sent to Kafka topic successfully!')
    }
