class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display(self):
        print(f"Car Details:")
        print(f"Make  : {self.make}")
        print(f"Model : {self.model}")
        print(f"Year  : {self.year}")
        print(f"Color : {self.color}")

class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity):
        super().__init__(make, model, year, color)  # Initialize from parent class
        self.battery_capacity = battery_capacity     # in kWh

    def display(self):
        super().display()  # Call the parent class display method
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Example usage
my_electric_car = ElectricCar("Tesla", "Model 3", 2022, "White", 75)
my_electric_car.display()
