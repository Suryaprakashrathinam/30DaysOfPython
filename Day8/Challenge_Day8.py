from  import Car

car1 = Car("Honda", "City", 2022, "Blue")
car2 = Car("Tesla", "Mustang", 2025, "Red")

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.colour)
car1.drive()
car1.stop()

print(car2.make)
print(car2.model)
print(car2.year)
print(car2.colour)
car2.drive()
car2.stop()