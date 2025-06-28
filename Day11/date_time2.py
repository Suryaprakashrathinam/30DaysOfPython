from datetime import date, datetime, time

today = date.today()
print("Today is:", today)
print("day:", today.day)
print("month:", today.month)
print("year:", today.year)

print(today.strftime("%A, %dth of %B %Y")) #this is derived from datetime documentation from G

next_year = today.replace(year = today.year + 1) #same with next year
print(next_year)

difference = abs(next_year - today) #to find days difference between 2 years
print("Only {} days untill next year".format(difference.days)) #not confuss with above. this is different

my_birthday = date (1995, 5, 29) #here arguments are passed
my_birthday = date.fromisoformat("1995-05-29") #here strings are passed
print("I was born on:", my_birthday)
print(my_birthday.weekday()) #result we will get 0 because monday consider as 0 in python.

now = datetime.now()
print("Right now is:", now)
print("It's the {}th minute of the {}th hour, of the {}th day of the {}th month".format(
    now.minute,
    now.hour,
    now.day,
    now.month
))

operation_sindoor = datetime.fromisoformat("2025-05-07 01:30:00:000+05:30") #op sindoor with indian time zone
print("Operation sindoor was conducted by India on:", operation_sindoor)

print(operation_sindoor.strftime("Operation Sindoor was conducted on %A %B %dth, %Y at %XAM MSD(%Z)"))
'''above %X for combination of hour,min,sec; MSD(%Z) is for time zone'''
print("MSD is actually:", operation_sindoor.tzinfo)

my_time = time(15, 33, 5) #similar to date args are passed
my_time = time.fromisoformat("15:33:05-05:30") #05:30 is time zone
print(my_time)
print(my_time.strftime("%I:%M %p")) #convert 24 hr time zone into 12 hr time zone with am & pm indication.

my_date = date(2022, 5, 22) #combined date object with time object
abi_bday = datetime.combine(my_date, my_time)
print(abi_bday)