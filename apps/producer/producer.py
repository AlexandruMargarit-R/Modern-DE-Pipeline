from pathlib import Path

from kafka import KafkaProducer

script_dir = Path(__file__).resolve().parent
file_path = script_dir.parents[1] / "data" / "bookings.csv"

TOPIC_NAME = "modern-pipeline"
BOOTSTRAP_SERVERS = "localhost:19092"
REQUEST_TIMEOUT_MS = 5000

try:

    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS, request_timeout_ms=REQUEST_TIMEOUT_MS
    )

    print("Producer created successfully.")
    with open(file_path, "r") as f:
        f.readline()
        for line in f:
            producer.send(TOPIC_NAME, line.encode("utf-8"))
            print(f"Message sent successfully: {line.strip()}")

    producer.close()
except Exception as e:
    print(f"An error occurred: {e}")
