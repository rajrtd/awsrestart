from classes import Car, IceCar, ElectricCar 

def main():
    my_ev = ElectricCar(brand = "Tesla", mileage_km = 10000, range="400,000")
    print(my_ev.__dict__)
    

if __name__ == "__main__":
    main()