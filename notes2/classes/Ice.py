from .Car import Car

class IceCar(Car):
    def __init__(self, brand, mileage_km, fuel_consumption, fuel_level):
        super().__init__(brand, mileage_km)
        self.fuel_consumption = fuel_consumption
        self.fuel_level = fuel_level