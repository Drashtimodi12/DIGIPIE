from datetime import date, time, datetime, timedelta

today = date.today()
print("Today is", today)                # OP: Today is 2025-11-27
print("Today Year is: ", today.year)    # OP: Today Year is:  2025
print("Today Month is: ",today.month)   # OP: Today Month is:  11
print("Today Day is: ",today.day)       # OP: Today Day is:  27

print("\n===========================\n")


d = datetime.now()
print("Today date and timing is: ", d) # OP: Today date and timing is: 2025-11-27 17:18:30.591293
print("Today date is: ", d.date())     # OP: Today date is: 2025-11-27
print("Today time is: ", d.time())     # OP: Today time is: 17:18:30.591293 
print("Today hour is: ", d.hour)       # OP: Today hour is: 17
print("Today Year is: ", d.year)       # OP: Today Year is:  2025
print("Today Month is: ", d.month)     # OP: Today Month is:  11
print("Today Day is: ", d.day)         # OP: Today Day is:  27



print("\n===========================\n")


"""
Formatting Dates (Convert date → String)    Use strftime() to format:
%d	Day	        01–31
%m	Month	    01–12
%Y	Year(full)	2025
%H	Hour(24hr)	14
%M	Minute	    59
%S	Second	    45
%B	Full month name	    November
"""
now = datetime.now()
print(now.strftime("%d-%m-%Y"))   # 27-11-2025
print(now.strftime("%B %d, %Y"))  # November 27, 2025
print(now.strftime("%H:%M:%S"))   # 17:30:45


print("\n===========================\n")



"""
What is timedelta in Python?
    timedelta represents a duration — the amount of time between two dates or times.

Why do we use timedelta?
    Add/subtract days from a date
    Find difference between two dates
    Calculate expiry dates
    Find age, work duration, billing hours, etc.

You can create a timedelta using:
    timedelta(days, hours, minutes, seconds)
"""