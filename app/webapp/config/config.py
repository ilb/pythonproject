import inject
from inject import Binder

from webapp.services.timeservice import TimeService

def init() -> None:
     inject.configure(build_container)

def build_container(binder: Binder) -> Binder:
     binder.bind(TimeService, TimeService())
     return binder
 
def host() -> str:
    return "127.0.0.1"

def port() -> int:
    return 8000
