import time

from webapp.services.timeservice import TimeService

def test_get_date():
    instance = TimeService()
    assert time.strftime("%H:%M") == instance.get_time()
