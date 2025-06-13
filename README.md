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

## 🔧 Tech Stack

| Layer         | Tools Used                                      |
|---------------|------------------------------------------------|
| Producer      | Python (simulated Kafka producers)              |
| Stream Engine | Apache Kafka, PySpark                           |
| Storage       | PostgreSQL, AWS S3 (optional)                   |
| API Layer     | Flask or Django                                 |
| Frontend      | React or HTML/CSS (optional)                    |
| DevOps        | Docker, Jenkins, Kubernetes (optional)          |
