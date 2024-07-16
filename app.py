from flask import Flask, request, jsonify
import pymongo
from datetime import datetime

app = Flask(__name__)

MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DB = 'upswing_mqtt_db'
MONGO_COLLECTION = 'upswing_statuses'

mongo_client = pymongo.MongoClient(MONGO_URI)
mongo_db = mongo_client[MONGO_DB]
mongo_collection = mongo_db[MONGO_COLLECTION]


@app.route('/')
def index():
    return {"message": "Welcome to the MQTT status count API"}


@app.route('/status_count', methods=['GET'])
def get_status_count():
    start = request.args.get('start')
    end = request.args.get('end')

    if not start or not end:
        return jsonify({"error": "start and end query parameters are required"}), 400

    try:
        start_dt = datetime.fromisoformat(start)
        end_dt = datetime.fromisoformat(end)
    except ValueError:
        return jsonify({"error": "Invalid date format. Use ISO format: YYYY-MM-DDTHH:MM:SS"}), 400

    pipeline = [
        {"$match": {"timestamp": {"$gte": start_dt, "$lt": end_dt}}},
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
    ]

    results = list(mongo_collection.aggregate(pipeline))
    status_counts = {result["_id"]: result["count"] for result in results}

    return jsonify(status_counts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
