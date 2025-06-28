'''Used to perform multiple tasks concurrently (like multitasking). Good for I/O (input/output)
bound tasks like reading files and fetching data from API'''

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking the {first} {last}")

def take_out_trash():
    time.sleep(4)
    print("You take out the trash")

def get_mail():
    time.sleep(2)
    print("You get the mail")

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()
# walk_dog()
# take_out_trash()
# get_mail()
chore1.join()
chore2.join()
chore3.join()
print("All works are completed!")
