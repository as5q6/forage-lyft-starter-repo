from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def needs_service(self):
        return self.service_date_exceeded(2) or self.engine_should_be_serviced()
