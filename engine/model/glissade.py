from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Glissade(WilloughbyEngine):
    def needs_service(self):
        return self.service_date_exceeded(3) or self.engine_should_be_serviced()

    def tires_need_service(self, tire_wear):
        return max(tire_wear) >= 0.9