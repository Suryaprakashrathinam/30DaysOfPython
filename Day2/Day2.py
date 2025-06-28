# 🗒 Topics
# Integers, floats, strings, booleans, type conversion

#  Challenge
# Calculate the area of a rectangle using user-input length and width

# inputs
length = float (input("Enter the length of the rectangle: "))
width = float (input("Enter the width of the rectangle: "))
unit = input ("Enter the unit(Eg. mm, cm, m): ")

# formula of rectangle
# Area = length * width
area = length * width

# resullt
print(f"Area of the rectangle is {area} square {unit}")
