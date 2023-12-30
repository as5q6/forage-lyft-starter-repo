from datetime import datetime

from engine.sternman_engine import SternmanEngine


class Palindrome(SternmanEngine):
    def needs_service(self):
        return self.service_date_exceeded(2) or self.engine_should_be_serviced()
