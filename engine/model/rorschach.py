from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Rorschach(WilloughbyEngine):
    def needs_service(self):
        return self.service_date_exceeded(2) or self.engine_should_be_serviced()
