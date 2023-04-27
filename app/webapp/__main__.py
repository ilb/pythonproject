import logging
import os
import sys
from os.path import dirname, realpath

import yaml
from bottle import Bottle, static_file
from bottle_swagger import SwaggerPlugin

if __package__ == "__main__":
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

from app.webapp.config import config
from app.webapp.api.controllers.time import time
from app.webapp.api.controllers.heartbeat import heartbeat

webapp = Bottle()


def main():
    try:
        config.init()
        # mounting controllers
        webapp.mount("/webapp/time/", time)
        webapp.mount("/webapp/heartbeat", heartbeat)
        # disable before release!
        if config.test_mode():
            webapp.install(build_swagger_plugin())

        sys.exit(
            webapp.run(
                server="gunicorn",
                host=config.host(),
                port=config.port(),
                debug=True,
            )
        )
    except (KeyboardInterrupt, SystemExit):
        exit(0)
    except Exception as ex:
        logging.error(f"Unhandled Exception {ex}")
        raise ex


def build_swagger_plugin():
    with open(dirname(realpath(__file__)) + "/docs/openapi.yaml", "r") as stream:
        swagger = yaml.full_load(stream.read())
        return SwaggerPlugin(
            swagger,
            validate_swagger_spec=False,
            serve_swagger_ui=True,
            swagger_ui_suburl="/webapp/swagger/",
        )


@webapp.route("/webapp/", method='GET', skip=True)
def base_page():
    return static_file("index.html", root=(dirname(realpath(__file__)) + "/docs/"))


if __name__ == "__main__":
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)
    main()
