#!/opt/anaconda3/bin/python

import os
import sys
import json
import bottle
from bottle import route, run, request
from bottle_swagger import SwaggerPlugin

if __name__.startswith("__main__"):
    os.chdir(os.path.dirname(__file__))
    sys.path.append("..")

    import module

with open("../docs/openapi.json", "r") as spec:
    swagger_spec = json.loads(spec.read())
    bottle.install(
        SwaggerPlugin(
            swagger_spec,
            validate_swagger_spec=False,
            serve_swagger_ui=True,
            swagger_ui_suburl="/swagger/",
        )
    )


@route("/time")
def get_time():
    return {"time": module.get_time()}


run(server="cgi")
