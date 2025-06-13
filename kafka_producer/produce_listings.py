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

TOPIC = 'product_listings'
categories = ['electronics', 'fashion', 'home', 'books', 'beauty']

while True:
    listing = {
        "product_id": random.randint(1000, 1100),
        "name": fake.word(),
        "category": random.choice(categories),
        "price": round(random.uniform(5.0, 500.0), 2),
        "timestamp": fake.iso8601()
    }
    print(f"Sending listing: {listing}")
    producer.send(TOPIC, listing)
    time.sleep(5)
