import time
from app import module

class TestModule():

    def test_get_date(self):
        assert time.strftime("%H:%M") == module.get_time()
