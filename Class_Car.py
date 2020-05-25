class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name = str(self.year)+ " "+self.make+ " "+self.model
        return long_name

    def read_odometer(self):
        print("This car have " + str(self.odometer_reading)+ "  miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("It's a trick!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super.init(self, make, model, year)


my_new_car= Car("audi", "q4", 2018)

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23500)
my_new_car.increment_odometer(100)                      
my_new_car.read_odometer()
