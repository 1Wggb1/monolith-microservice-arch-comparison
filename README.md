## Commands to configure and install required dependencies
This project uses `python 3.11+`;

### Creating a python virtual environment
- `python3 -m venv venv`

### Activating venv
- `source venv/bin/activate`

### Installing required project deps
- `pip install -r requirements.txt`

### Running application
**OBS: Execute at root level**

## Monolith
- `cd ./docker/monolith && docker compose up -d`

## Microservice
- `cd ./docker/microservice && docker compose up -d`

### Running load test
## Monolith
- `cd ./load-test/monolith && docker run --network=monolith_monolith-network --rm -i grafana/k6 run - <k6-test-script.js`
- `cd ./load-test/monolith && docker run --network=monolith_monolith-network --rm -i grafana/k6 run - <k6-test-script-create.js`

## Microservice
- `cd ./load-test/microservice && docker run --network=microservice_microservice-network --rm -i grafana/k6 run - <k6-test-script.js`
- `cd ./load-test/microservice && docker run --network=microservice_microservice-network --rm -i grafana/k6 run - <k6-test-script-create.js`