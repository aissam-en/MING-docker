import os
import time
import random
import sys
import paho.mqtt.client as mqtt
import multiprocessing

def on_connect(client, userdata, flags, rc):
    print(f"Client {client.client_id} connected with result code {rc}")

def create_and_run_client(client_id, broker_url, publish_topic, data):
    mqttc = mqtt.Client(client_id)
    mqttc.on_connect = on_connect
    mqttc.connect(broker_url)

    while True:
        for power in data:
            mqttc.publish(publish_topic, power)
            print(f"Client {client_id}: New power value: {power} ==> added to MQTT_TOPIC: '{publish_topic}'")
            time.sleep(1)

if __name__ == "__main__":
    # Number of client processes to generate, default is 10 if not specified in NUM_CLIENTS in docker-compose.yml.
    num_clients = int(os.environ.get("NUM_CLIENTS", 10)) 

    # MQTT broker URL ("emqx" is the DNS name) , because the services (emqx, influxdb, grafana, ...) connect to the same Docker network, so we can use there name as dns name. Default is "emqx", we can also modified in MQTT_BROKER_URL in docker-compose.yml.
    broker_url = os.environ.get("MQTT_BROKER_URL", "emqx")  
    # broker_url = "mqtt.eclipseprojects.io" # this is a public online mqtt brocker, other option.
    
    # "power" is the name of MQTT topic for publishing, default is "power", or as specified in MQTT_PUBLISH_TOPIC in docker-compose.yml.
    publish_topic = os.environ.get("MQTT_PUBLISH_TOPIC", "power") 

    # fake data: 50 < data < 300:
    data = [221, 146, 283, 182, 86, 274, 243, 140, 264, 239, 64, 100, 98, 199, 300, 214, 204, 69, 275, 242, 107, 98, 225, 62, 193, 220, 108, 133, 184, 288, 227, 73, 290, 248, 256, 247, 237, 273, 77, 270, 238, 211, 232, 138, 216, 152, 154, 217, 193, 59]

    # Create and start clients processes
    processes = []
    for i in range(num_clients):
        client_id = f"client_{i}"
        process = multiprocessing.Process(target=create_and_run_client, args=(client_id, broker_url, publish_topic, data))
        process.start()
        processes.append(process)