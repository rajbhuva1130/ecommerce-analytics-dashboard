from kafka import KafkaProducer
from faker import Faker
import json
import random
import time

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC = 'feedback'

while True:
    feedback = {
        "feedback_id": fake.uuid4(),
        "product_id": random.randint(1000, 1100),
        "user_id": fake.uuid4(),
        "rating": random.randint(1, 5),
        "comment": fake.sentence(),
        "timestamp": fake.iso8601()
    }
    print(f"Sending feedback: {feedback}")
    producer.send(TOPIC, feedback)
    time.sleep(3)
