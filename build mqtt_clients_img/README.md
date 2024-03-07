# Build simple MQTT clients docker image 'mqtt_clients_img'
We will use docker-compose.yml to build our 'mqtt_clients_img' image and test it.

### Build docker image :
```bash
docker-compose build
```
Now our docker image is successfully built.

### Test docker image :
```bash
docker-compose up
```

then, two containers will be created to test if our image works.
open emqx dashboard to see: http://localhost:18083

### Access EMQX dashboard to verify :
http://localhost:18083

