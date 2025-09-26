import math
import os
import time
import datetime
def date_reminder():
    while True:
        date_str = input("Enter a date (YYYY-MM-DD): ").strip()
        try:
            target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            today = datetime.date.today()
            remaining_days = (target_date - today).days
            if remaining_days< 0:
                print("The date has already passed.")
                break
            elif remaining_days == 0:
                print("The date is today!")
            else:
                print(f"The date is in {remaining_days} days.")
            filename = "reminder.txt"
            with open(filename, 'a') as f:
                f.write(f"Date: {target_date}, Days remaining: {remaining_days}\n")
            print(f"Reminder saved to {filename}.\n")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")