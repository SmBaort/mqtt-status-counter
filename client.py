import paho.mqtt.client as mqtt
import random
import json
import time

MQTT_BROKER = "localhost"
MQTT_TOPIC = "status_topic"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection succeed for rc:", rc)
    else:
        print("Connection failed for rc:", rc)


mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.connect(MQTT_BROKER)

try:
    mqtt_client.loop_start()
    while True:
        status = random.randint(0, 6)
        message = {"status": status}
        mqtt_client.publish(MQTT_TOPIC, json.dumps(message))
        print("message: ",message)
        time.sleep(1)
except KeyboardInterrupt:
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
