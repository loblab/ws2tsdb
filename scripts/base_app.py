import argparse
import signal
import time
import sys
import os
import logging

class BaseApp:

    def __init__(self, id, description):
        signal.signal(signal.SIGINT, self.sig_handler)
        signal.signal(signal.SIGTERM, self.sig_handler)
        self.quit_flag = False
        sfile = sys.argv[0]
        ver = time.strftime('Ver %Y/%m/%d %H:%M %Z', time.localtime(os.path.getmtime(sfile)))
        self.argps = argparse.ArgumentParser(description=description)
        self.argps.add_argument('-V', '--version', action='version', version=ver)
        self.argps.add_argument('-D', '--debug', action='store_true',
                help="output more logs (debug level)")
        self.base_init()
        self.init()
        self.args = self.argps.parse_args()
        try:
            self.id = self.args.id
        except:
            self.id = id
        self.init_logger()
        self.log.info(description)
        self.log.info(ver)
        if self.args.debug:
            self.log.setLevel(logging.DEBUG)
            self.log.debug("Debug log on")

    def init_logger(self):
        self.log = logging.getLogger(self.id)
        self.log.setLevel(logging.INFO)

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
               datefmt='%m/%d/%Y %H:%M:%S')
        ch.setFormatter(formatter)
        self.log.addHandler(ch)

    def quit(self):
        self.log.debug("Going to quit...")
        self.quit_flag = True

    def sig_handler(self, signum, frame):
        self.log.info("Got signal %d" % signum)
        self.quit()

    def base_init(self):
        pass

    def init(self):
        pass

    def startup(self):
        self.log.info("Startup...")

    def cleanup(self):
        self.log.info("Cleanup...")

    def main(self):
        self.startup()
        while not self.quit_flag:
            time.sleep(1)
        self.cleanup()

