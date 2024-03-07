# MING-docker
Docker configurations for MING (MQTT, Influxdb, Node-Red and Grafana) project

## First, setting up the mqtt_clients_img docker image :
There are two options for setting up the mqtt_clients_img docker image:
### 1. Building from Dockerfile :
Navigate to the `./build mqtt_clients_img` folder.
Run the following command:
```bash
docker-compose up
```
(If you want to make changes in the codes).

### 2. Pulling it from docker hub :
The mqtt_clients_img in available on docker hub too.
To pull it from docker hub:
```bash
docker pull aissamen/mqtt_clients_img
```
if you follow the second option, make this changes : 
Replace `mqtt_clients_img` by `aissamen/mqtt_clients_img` in [docker-compose.yml](docker-compose.yml)
From
```bash
mqtt_clients:
    image: mqtt_clients_img
    ...
```
To : 
```bash
mqtt_clients:
    image: aissamen/mqtt_clients_img
    ...
```

Note: 
For instructions to build and test the mqtt_clients_img image separately, see the [README.md](build%20mqtt_clients_img/README.md) in the `/build mqtt_clients_img` folder.


