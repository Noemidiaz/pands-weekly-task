# weekday.py
#
# Author: Noemi Diaz

#Import python's datetime

import datetime

# weekdays definition
weekday = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

# Date of today
today = datetime.datetime.today()

if today.weekday() == 4:

    print ("Yes, today is a weekday")

elif today.weekday() == 5 or today.weekday() == 6:
    
    print ("Hooray!It's finally weekend!")
    