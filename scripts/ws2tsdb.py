#!/usr/bin/env python3
import sys
import time
import asyncio
import websockets
import json
from tsdb_app import *

ID = "ws2tsdb"
DESC = "Receive data via WebSocket, and save to InfluxDB"

class App(TsdbApp):

    def init(self):
        self.argps.add_argument('-r', '--uri', dest='uri', type=str,
                help="WebSocket url to get the input")
        self.argps.add_argument('-i', '--input', dest='input', type=str,
                help="The field name to get from the input")
        self.argps.add_argument('-t', '--table', dest='table', type=str,
                help="Database table name")
        self.argps.add_argument('-o', '--output', dest='output', type=str,
                help="The field name to save as")

    def cleanup(self):
        pass

    async def loop(self):
        async with websockets.connect(self.args.uri) as websocket:
            await websocket.send("version")
            msg = await websocket.recv()
            obj = json.loads(msg)
            if obj["type"] == "version":
                self.log.info(obj["version"])
            while not self.quit_flag:
                msg = await websocket.recv()
                if type(msg) == str:
                    obj = json.loads(msg)
                    ts = time.ctime(obj["time"] / 1000.0)  # time field in millisecond
                    #print(ts)
                    if obj["type"] == "status":
                        val = obj[self.args.input]
                        self.save(val, ts)

    def process(self):
        self.log.info("%s:%s => %s.%s:%s", self.args.uri, self.args.input,
                self.args.data, self.args.table, self.args.output)
        asyncio.get_event_loop().run_until_complete(
            self.loop())

    def save(self, val, ts):
        points = [{
            "measurement": self.args.table,
            "time": ts,
            "tags": {
                "source": self.args.output,
            },
            "fields": {
                "value": val,
            },
        }]
        self.tsdb.write_points(points)

    def main(self):
        self.startup()
        self.process()
        self.cleanup()
        self.log.info("Application quit.")

if __name__ == "__main__":
    app = App(ID, DESC)
    sys.exit(app.main())

