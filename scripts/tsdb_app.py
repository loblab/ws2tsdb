#!/usr/bin/python3
from influxdb import InfluxDBClient
from base_app import *

class TsdbApp(BaseApp):

    DEFAULT_HOST = "influxdb"
    DEFAULT_PORT = 8086
    DEFAULT_DATA = "ws2tsdb"
    DEFAULT_USER = ""
    DEFAULT_PSWD = ""

    def base_init(self):
        self.argps.add_argument('-s', '--host', dest='host', type=str, default=self.DEFAULT_HOST,
            help="InfluxDB server address. default '%s'" % self.DEFAULT_HOST)
        self.argps.add_argument('-p', '--port', dest='port', type=int, default=self.DEFAULT_PORT,
            help="InfluxDB server port. default %d" % self.DEFAULT_PORT)
        self.argps.add_argument('-d', '--data', dest='data', type=str, default=self.DEFAULT_DATA,
            help="InfluxDB server database. default '%s'" % self.DEFAULT_DATA)
        self.argps.add_argument('-u', '--user', dest='user', type=str, default=self.DEFAULT_USER,
            help="InfluxDB server user name. default '%s'" % self.DEFAULT_USER)
        self.argps.add_argument('-w', '--pswd', dest='pswd', type=str, default=self.DEFAULT_PSWD,
            help="InfluxDB server password. default '%s'" % self.DEFAULT_PSWD)

    def startup(self):
        self.log.info("Connect to InfluxDB (%s:%d)...", self.args.host, self.args.port)
        self.tsdb = InfluxDBClient(self.args.host, self.args.port,
                self.args.user, self.args.pswd, self.args.data)


