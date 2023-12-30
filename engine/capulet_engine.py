
from engine import Engine
from car import Car

MILEAGE_THRESHOLD_CAPULET = 30000


class CapuletEngine(Engine):
    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > MILEAGE_THRESHOLD_CAPULET
