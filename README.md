# WebSocket to InfluxDB

Read data from WebSocket, save to InfluxDB

- Platform: Python 3.7, InfluxDB, Grafana
- Ver: 0.1
- Updated: 9/28/2019
- Created: 9/28/2019
- Author: loblab

## Usage

- See [my project 'tsdb'](https://github.com/loblab/tsdb) to create InfluxDB & Grafana servers
- Config docker/docker-compose.yml
- In docker directory, run
```bash
docker-compose up -d
```

## Remarks

- asyncio need python 3.7 or above
- input data format is json string

