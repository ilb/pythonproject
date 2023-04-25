"""
Example of usecase
"""
import inject

from app.webapp.services.timeservice import TimeService


class SendToTimeService:

    @inject.autoparams()
    def __init__(self, time_service: TimeService):
        self.time_service = time_service

    def time_usecase(self):
        return self.time_service.get_time()
