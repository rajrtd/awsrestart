from .Car import Car

class ElectricCar(Car):
    def __init__(self, brand, mileage_km, range):
        super().__init__(brand, mileage_km)
        self.range=range
