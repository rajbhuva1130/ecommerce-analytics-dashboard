# 🛒 Real-Time E-Commerce Analytics Dashboard

A real-time analytics dashboard built using Python, Apache Kafka, PySpark, PostgreSQL, and Flask/Django. This project simulates a mini eBay-style system to showcase real-time data ingestion, processing, and insights delivery.

---

## 🚀 Project Overview

This system simulates and processes e-commerce events like:
- Customer transactions
- Product listings
- Customer feedback

The goal is to build a **streaming data pipeline** that processes and visualizes real-time metrics such as:
- Top-selling products
- Total revenue
- Average product rating
- Live transaction volume

---

## 🧱 Architecture

```text
+----------------+      +------------+      +------------+      +-------------+
| Data Producers | ---> | Apache     | ---> | PySpark    | ---> | PostgreSQL  |
| (Kafka Topics) |      | Kafka      |      | Streaming  |      |             |
+----------------+      +------------+      +------------+      +-------------+
                                             |
                                             V
                                    +-------------------+
                                    | Flask/Django API  |
                                    +-------------------+
                                             |
                                             V
                                    +-------------------+
                                    | Dashboard (React) |
                                    +-------------------+

---

## 🧰 Tech Stack

| Layer        | Tools Used                       |
|--------------|----------------------------------|
| Producers    | Python, Faker, Kafka-Python      |
| Streaming    | Apache Kafka, PySpark            |
| Storage      | PostgreSQL, AWS S3 (optional)    |
| API Layer    | Flask or Django                  |
| Dashboard    | React (optional)                 |
| DevOps       | Docker, Docker Compose, Jenkins  |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/rajbhuva1130/ecommerce-analytics-dashboard.git
cd ecommerce-analytics-dashboard

text

### 2. Install Python Dependencies

pip install kafka-python faker

text
> **Note:**  
> If using Python 3.11 or later, ensure the `Scripts` directory is in your `PATH` if Faker warnings appear.

---

## 🐳 Kafka Setup with Docker

### 3. Start Kafka and Zookeeper (Docker)

cd docker
docker-compose up -d

text
- Kafka: `localhost:9092`
- Zookeeper: `localhost:2181`

### 4. (Optional) Create Kafka Topics

docker exec -it docker-kafka-1 kafka-topics --create --topic transactions --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

docker exec -it docker-kafka-1 kafka-topics --create --topic product_listings --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

docker exec -it docker-kafka-1 kafka-topics --create --topic feedback --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

text

---

## 💡 Run the Project

### 5. Start Kafka Producers (Run in 3 separate terminals)

python kafka_producer/produce_transactions.py
python kafka_producer/produce_listings.py
python kafka_producer/produce_feedback.py

text
- Each script sends simulated real-time data into its Kafka topic.

---

## 🧹 Stopping & Cleaning Up

### 6. Stop the Kafka Environment

cd docker
docker-compose down

text

### 7. Stop Producers

- Press `Ctrl + C` in each terminal where producers are running.

---

## 🧭 Next Milestones

- Add PySpark streaming jobs to consume and transform Kafka data
- Store insights in PostgreSQL
- Build REST API to serve dashboard metrics
- (Optional) Create a React-based frontend dashboard

---

## 👤 Author

**Rajkumar Bhuva**  
📧 rrb.bhuva@gmail.com  
[LinkedIn](https://www.linkedin.com/in/rajkumar-bhuva-5b7480172/)
