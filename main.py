# Works only on windows

from win10toast import ToastNotifier
import datetime
import time

# Create a toast notifier object
toaster = ToastNotifier()

# Name
name = input("Enter your name: ")
name = name.title()

# How many times to display the notification?
howMany = int(input("How many times would I remind you to drink water? "))

# After how many minutes to display the notification?
notificationTime = int(input(f"In how many min(s) would you like me to remind you to drink water? "))

# Final Program to Loop
for i in range(howMany):
    # Loading the current timeCurrent time
    currentTime = datetime.datetime.now()
    timeNow = currentTime.strftime("%H:%M:%S")

    # Displaying the notification
    toaster.show_toast(f"Drink Water", f"Drink Water {name} its {timeNow}!", duration=10)
    # Waiting for the given time and again displaying notification
    time.sleep(notificationTime * 60)