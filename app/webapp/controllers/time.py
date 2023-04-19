import bottle
import inject
import json
import logging
import os
import sys
from bottle import route, run, request, Bottle
from logging import Logger
from webapp.services.timeservice import TimeService

logger: Logger = logging.getLogger(__name__)

time = Bottle()


@time.get("/")
@inject.autoparams()
def get_time(time_service: TimeService) -> dict:
    logger.info(f"time: {time_service.get_time()}")
    return {"time": time_service.get_time()}
