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

TOPIC = 'transactions'

while True:
    transaction = {
        "transaction_id": fake.uuid4(),
        "user_id": fake.uuid4(),
        "product_id": random.randint(1000, 1100),
        "amount": round(random.uniform(10.0, 500.0), 2),
        "timestamp": fake.iso8601()
    }
    print(f"Sending transaction: {transaction}")
    producer.send(TOPIC, transaction)
    time.sleep(1)
