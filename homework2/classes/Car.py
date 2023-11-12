class Car:
    def __init__(self, brand, mileage_km):
        self.brand=brand
        self.mileage_km=mileage_km

    def drive(self, distance_km):
        self.mileage_km += distance_km