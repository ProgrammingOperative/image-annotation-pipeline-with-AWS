from flask import Flask, request, jsonify, render_template_string, render_template
from kafka import KafkaConsumer, KafkaProducer
from threading import Thread
from queue import Queue, Empty
import io
import base64
from PIL import Image
import json

app = Flask(__name__)

# Kafka configuration
bootstrap_servers = '3.144.237.39:9092'
consumer_topic = 'demo_testing2'
producer_topic = 'labeled_image_topic'
group_id = 'image_consumer_group'

# Create a queue to store messages
message_queue = Queue()

# Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

def consume_messages():
    consumer = KafkaConsumer(
        consumer_topic,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id=group_id
    )
    for message in consumer:
        message_queue.put(message.value)

# Start the background thread to consume Kafka messages
consumer_thread = Thread(target=consume_messages, daemon=True)
consumer_thread.start()

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get an image for labeling
@app.route('/get_image', methods=['GET'])
def get_image():
    try:
        image_data = message_queue.get_nowait()  # Non-blocking get from the queue
        img = Image.open(io.BytesIO(image_data))
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        img_base64 = base64.b64encode(img_byte_arr).decode('utf-8')
        return jsonify({'image': img_base64})
    except Empty:
        return jsonify({'error': 'No images available'}), 404

# Route to post labeled image
@app.route('/label_image', methods=['POST'])
def label_image():
    data = request.json
    image_base64 = data['image']
    label = data['label']
    
    # Send image and label to another Kafka topic
    message = {
        'image': image_base64,
        'label': label
    }
    producer.send(producer_topic, value=json.dumps(message).encode('utf-8'))
    producer.flush()
    
    return jsonify({'status': 'Image and label sent successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
