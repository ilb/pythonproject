import os
import sys
import yaml
from bottle import Bottle
from os.path import dirname, realpath

if __package__ == "__main__":
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

from webapp.config import config
from webapp.controllers.time import time

app = Bottle()


def main():
    config.init()

    app.mount("/webapp/time/", time)

    sys.exit(
        app.run(
        server="gunicorn",
        host=config.host(),
        port=config.port(),
        debug=True,
    )
 )
