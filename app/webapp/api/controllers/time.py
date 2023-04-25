"""
Example of controller
"""

import logging
from logging import Logger

import inject
from bottle import Bottle

from app.webapp.usecases.timeservice_usecase import SendToTimeService

logger: Logger = logging.getLogger(__name__)

time = Bottle()


@time.get("/")
@inject.autoparams()
def get_time(time_service: SendToTimeService):
    logger.info(f"time: {time_service.time_usecase()}")
    return {"time": time_service.time_usecase()}
