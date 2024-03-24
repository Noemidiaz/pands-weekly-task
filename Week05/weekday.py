# weekday.py
#
# Author: Noemi Diaz


# Step 1: Import python's datetime

import datetime


# Step 2: Checking days of the week as a tuple or integer from 0 (Monday) to 6 (Sunday)

weekday = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")


# Step 3: Date of today

today = datetime.datetime.today()


# Step 4: Describing conditional statements

if today.weekday() == 4:

    print ("Yes, today is a weekday")

elif today.weekday() == 5 or today.weekday() == 6:
    
    print ("Hooray!It's finally weekend!")
