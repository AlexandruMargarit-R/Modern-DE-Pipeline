from kafka import KafkaConsumer

TOPIC_NAME = "modern-pipeline"
BOOTSTRAP_SERVERS = "localhost:19092"
REQUEST_TIMEOUT_MS = 5000

consumer = KafkaConsumer(
    bootstrap_servers=BOOTSTRAP_SERVERS, request_timeout_ms=REQUEST_TIMEOUT_MS
)

try:
    consumer.subscribe([TOPIC_NAME])
    print("Consumer subscribed to topic sucessfully.")
    for message in consumer:
        print(f"Received message: {message.value.decode('utf-8')}")
    consumer.close()
except Exception as e:
    print(f"An error occurred: {e}")
