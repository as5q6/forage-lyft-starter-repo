import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()
        self.current_mileage = 0
        self.last_service_mileage = 0
        self.car = Calliope(self.today, self.current_mileage, self.last_service_mileage)

    def test_spindler_battery_service(self):
        self.car.last_service_date = self.today.replace(year=self.today.year - 3)
        self.assertTrue(self.car.needs_service())

    def test_carrigan_tire_service(self):
        self.car.tire_wear = [0.9, 0.8, 0.7, 0.6]
        self.assertTrue(self.car.tires_need_service())

    def test_octoprime_tire_service(self):
        self.car.tire_wear = [0.8, 0.8, 0.8, 0.8]
        self.assertTrue(self.car.tires_need_service())

    def test_battery_should_be_serviced(self):
        self.car.last_service_date = self.today.replace(year=self.today.year - 3)
        self.assertTrue(self.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.car.last_service_date = self.today.replace(year=self.today.year - 1)
        self.assertFalse(self.car.needs_service())

    def test_engine_should_be_serviced(self):
        self.car.current_mileage = 30001
        self.assertTrue(self.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.car.current_mileage = 30000
        self.assertFalse(self.car.needs_service())

    def test_engine_at_service_limit(self):
        self.car.current_mileage = 30000
        self.assertFalse(self.car.needs_service())


class TestGlissade(TestCalliope):
    def setUp(self):
        self.today = datetime.today().date()
        self.current_mileage = 0
        self.last_service_mileage = 0
        self.car = Glissade(self.today, self.current_mileage, self.last_service_mileage)


class TestPalindrome(TestCalliope):
    def setUp(self):
        self.today = datetime.today().date()
        self.current_mileage = 0
        self.last_service_mileage = 0
        self.car = Palindrome(self.today, self.current_mileage, self.last_service_mileage)


class TestRorschach(TestCalliope):
    def setUp(self):
        self.today = datetime.today().date()
        self.current_mileage = 0
        self.last_service_mileage = 0
        self.car = Rorschach(self.today, self.current_mileage, self.last_service_mileage)


class TestThovex(TestCalliope):
    def setUp(self):
        self.today = datetime.today().date()
        self.current_mileage = 0
        self.last_service_mileage = 0
        self.car = Thovex(self.today, self.current_mileage, self.last_service_mileage)


if __name__ == '__main__':
    unittest.main()