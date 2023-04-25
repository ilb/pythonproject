import logging.config
from os.path import dirname, realpath

import inject
import yaml
from inject import Binder
from app.webapp.services.timeservice import TimeService


def init() -> None:
    _configure_logger()
    inject.configure(build_container)


def _configure_logger() -> None:
    with open(dirname(realpath(__file__)) + "/logger_conf.yaml", "r") as log_config:
        logging.config.dictConfig(yaml.full_load(log_config))


def build_container(binder: Binder) -> Binder:
    binder.bind(TimeService, TimeService())
    return binder


def host() -> str:
    return "127.0.0.1"


def port() -> int:
    return 8000


def test_mode() -> bool:
    return False
