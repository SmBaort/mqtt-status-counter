import pika
import pymongo
import json
from datetime import datetime

RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = 'mqtt_queue'
MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DB = 'upswing_mqtt_db'
MONGO_COLLECTION = 'upswing_statuses'

mongo_client = pymongo.MongoClient(MONGO_URI)
mongo_db = mongo_client[MONGO_DB]
mongo_collection = mongo_db[MONGO_COLLECTION]


connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=RABBITMQ_QUEUE)


def callback(ch, method, properties, body):
    message = json.loads(body)
    message["timestamp"] = datetime.utcnow()
    mongo_collection.insert_one(message)


channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)
print('wait for messages.')
channel.start_consuming()
