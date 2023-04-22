# Works only on windows

# Installing win10toast on your or some person's computer
import os
os.system("pip install win10toast") # Uncomment these three lines if win10toast module is not installed, if installed comment it out

from win10toast import ToastNotifier
import datetime
import time


# Create a toast notifier object
toaster = ToastNotifier()

# Name
name = input("Enter your name: ")
name = name.title()

# After how many minutes to display the notification?
notificationTime = int(input(f"In how many min(s) would you like me to remind you to drink water? "))

# # How many times to display the notification? (Uncomment for using for loop and comment for using while loop)
# howMany = int(input("How many times would I remind you to drink water? "))


# # Final Program to Loop

# for i in range(howMany):
#     # Loading the current timeCurrent time
#     currentTime = datetime.datetime.now()
#     timeNow = currentTime.strftime("%H:%M:%S")
#
#     # Displaying the notification
#     toaster.show_toast(f"Drink Water", f"Drink Water {name} its {timeNow}!", duration=10)
#     # Waiting for the given time and again displaying notification
#     time.sleep(notificationTime * 60)
# --------------------------OR---------------------------------

while True:
    # Loading the current timeCurrent time
    currentTime = datetime.datetime.now()
    timeNow = currentTime.strftime("%H:%M:%S")

    # Displaying the notification
    toaster.show_toast(f"Drink Water", f"Drink Water {name} its {timeNow}!", duration=10)
    # Waiting for the given time and again displaying notification
    time.sleep(notificationTime * 60)

# Either use for loop or use while loop for the program
