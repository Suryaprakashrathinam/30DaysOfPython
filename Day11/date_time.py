import datetime

date = datetime.date(1995, 5, 29)
today = datetime.date.today()
time = datetime.time(6, 00, 00)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %d-%m-%Y") #this is put and refered by the datetime documentation
print(date)
print(today)
print(time)
print(now)

target_datetime = datetime.datetime(2030, 5, 15, 12, 30, 25)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date NOT passed")