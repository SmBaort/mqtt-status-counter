# MQTT Status Counter

## Description

This project aims to develop a client-server script in Python that handles MQTT messages via RabbitMQ. The client script emits MQTT messages every second, containing a field "status" with a random value in the range of 0-6. The server processes these messages and stores them in MongoDB. Additionally, the server provides an endpoint to accept start and end times and return the count of each status during the specified time range.

## 🌟 Project Objectives:

### 1. MQTT Messaging Integration
- Implement MQTT messaging via RabbitMQ.
- Emit MQTT messages every second with a "status" field containing a random value between 0 and 6.

### 2. Message Processing
- Develop a server script to process incoming MQTT messages.
- Store the processed messages in MongoDB.

### 3. Data Retrieval Endpoint
- Create an endpoint to accept start and end times.
- Return the count of each status within the specified time range using MongoDB's aggregate pipeline.

## 🚀 Getting Started

### 1. Setup Your Environment

**Install Dependencies**

Make sure you have Python installed. Then, install the necessary packages:

```
pip install pika pymongo paho-mqtt flask
```

**Create a Virtual Environment**

To keep your project dependencies isolated, create and activate a virtual environment:

```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate` 
```

### 2. Install and Configure RabbitMQ

- **`Download and Install Erlang`**
- **`Download and Install RabbitMQ`**
- **`Enable MQTT Plugin`**
    ```
    rabbitmq-plugins enable rabbitmq_mqtt
    ```
- **`Restart RabbitMQ`**
    ```
    net stop RabbitMQ
    net start RabbitMQ
    ```
- **`Verify the Plugin`**
    ```
    rabbitmq-plugins list
    ```


### 3. Download and Install MongoDB
### 4. Run the Scripts
- **Start the MQTT client (`client.py`):**
```
python client.py
```

- **Start the MQTT consumer (`server.py`):**
```
python server.py
```

- **Start the Flask API (`app.py`):**
```
python app.py
```

### **API Endpoint:**

- `/status_count`
- Method: GET
- Parameters:
  - start: ISO format timestamp (e.g., 2024-01-01T00:00:00)
  - end: ISO format timestamp (e.g., 2024-07-17T01:00:00)
```
http://127.0.0.1:8000/status_count?start=2024-07-01T00:00:00&end=2024-07-17T01:00:00
```

## 📄 **License**
This project is licensed under the MIT License.
