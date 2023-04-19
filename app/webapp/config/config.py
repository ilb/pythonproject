import inject
import logging.config
import yaml
from inject import Binder
from os.path import dirname, realpath
from webapp.services.timeservice import TimeService


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
