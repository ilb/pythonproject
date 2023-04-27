import logging.config
from os.path import dirname, realpath

import inject
import yaml
from inject import Binder

from app.webapp.services.timeservice import TimeService
from pycontext import shared_context


def init() -> None:
    _configure_logger()
    inject.configure(build_container)
    shared_context.init(dirname(realpath(__file__)) + "/web.xml")


def _configure_logger() -> None:
    with open(dirname(realpath(__file__)) + "/logger_conf.yaml", "r") as log_config:
        logging.config.dictConfig(yaml.full_load(log_config))


def build_container(binder: Binder) -> Binder:
    binder.bind(TimeService, TimeService())
    return binder


def host() -> str:
    return shared_context.get("apps.pythonproject.host")


def port() -> int:
    return shared_context.get("apps.pythonproject.port")


def test_mode() -> bool:
    return shared_context.get("apps.pythonproject.test_mode")


def db() -> str:
    return shared_context.get("apps.pythonproject.db")


def db_password() -> str:
    return shared_context.get("apps.pythonproject.db_PASSWORD")


def db_user() -> str:
    return shared_context.get("apps.pythonproject.db_user")
