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
    return shared_context.get("apps.webapp.host")


def port() -> int:
    return shared_context.get("apps.webapp.port")


def test_mode() -> bool:
    return shared_context.get("apps.webapp.test_mode")


def db() -> str:
    return shared_context.get("apps.webapp.db")


def db_password() -> str:
    return shared_context.get("apps.webapp.db_PASSWORD")


def db_user() -> str:
    return shared_context.get("apps.webapp.db_user")


def file_folder() -> str:
    return shared_context.get("apps.webapp.file_folder")