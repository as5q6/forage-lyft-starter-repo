from abc import ABC
import datetime
from car import Car

class Engine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def service_date_exceeded(self, years):
        return (datetime.today().date() - self.last_service_date).days > years * 365

    def needs_service(self, years):
        return self.service_date_exceeded(years) or self.engine_should_be_serviced()