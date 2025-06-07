from datetime import date, datetime, time

today = date.today()
print(today.strftime("%A, %dth of %B %Y"))

my_birthday = date (1995, 5, 29) #here arguments are passed
#my_birthday = date.fromisoformat("1995-05-29") #here strings are passed
print("I was born on:", my_birthday)

difference = abs(my_birthday - today)
print(difference)