import os
import sys
import json
import bottle
import inject
from bottle import route, run, request, Bottle

from webapp.services.timeservice import TimeService

time = Bottle()

@time.get("/")
@inject.autoparams()
def get_time(time_service: TimeService) -> dict:
    return {"time": time_service.get_time()}
