import logging
import os
from datetime import datetime
from logging import Logger

import bottle
import inject
from bottle import Bottle, response

from app.webapp.config import config
from app.webapp.usecases.fileservice_usecase import SendToFileService

logger: Logger = logging.getLogger(__name__)

loader = Bottle()

timestamp = datetime.now()


@loader.post("/")
@inject.autoparams()
def load_file(file_usecase: SendToFileService):
    if "test_file" not in bottle.request.files:
        logger.error("File wasn't loaded.")
        response.status_code = 450
        return "File wasn't loaded."
    try:
        os.mkdir(f"{config.file_folder()}/{timestamp}")
    except OSError as os_error:
        logger.error("Unable to create directory")
        print(os_error)

    test_file = bottle.request.files["test_file"].file.read()

    with open(f"{config.file_folder()}/{timestamp}/test_file", "wb+") as file:
        file.write(test_file)
        logger.info("File successfully saved")

    status = file_usecase.send_file_usecase(test_file)
    if status == 200:
        response.status_code = 200
        return 200
    else:
        response.status_code = 450
        return 450
