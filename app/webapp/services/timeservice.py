"""
Example service
"""

import time

class TimeService:

    def get_time(self):
        return time.strftime("%H:%M")
