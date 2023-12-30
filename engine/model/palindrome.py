from datetime import datetime

from engine.sternman_engine import SternmanEngine


class Palindrome(SternmanEngine):
    def needs_service(self):
        return self.service_date_exceeded(3) or self.engine_should_be_serviced()

    def tires_need_service(self, tire_wear):
        return sum(tire_wear) >= 3