# Installing win10toast on your or some person's computer

from notifypy import Notify
import datetime
import time


# Create a toast notifier object
notification = Notify()

# Name
name = input("Enter your name: ")
name = name.title()

# After how many minutes to display the notification?
notificationTime = int(input(f"In how many min(s) would you like me to remind you to drink water? "))

while True:
    # Loading the current timeCurrent time
    currentTime = datetime.datetime.now()
    timeNow = currentTime.strftime("%H:%M:%S")

    # Displaying the notification
    notification.title = f"Drink Water {name}!!"
    notification.message = f"Drink Water it's {timeNow} you drank water {notificationTime} mins ago !!"
    notification.icon = "water-drop.png"
    notification.send()

    # Waiting for the given time and again displaying notification
    time.sleep(notificationTime * 60)

# Either use for loop or use while loop for the program
