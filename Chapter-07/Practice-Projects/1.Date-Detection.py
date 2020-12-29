# Date Detection

# Write a regular expression that can detect dates in the DD/MM/YYYY format.
# Assume that the days range from 01 to 31, the months range from 01 to 12, and 
# the years range from 1000 to 2999. Note that if the day or month is a single digit, 
# it’ll have a leading zero.

# The regular expression doesn’t have to detect correct days for each month or for leap years; 
# it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into 
# variables named month, day, and year, and write additional code that can detect if it is a valid date. 
# April, June, September, and November have 30 days, February has 28 days, and the rest of the months 
# have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, 
# except for years evenly divisible by 100, unless the year is also evenly divisible by 400. 
# Note how this calculation makes it impossible to make a reasonably sized regular expression that 
# can detect a valid date.

import re

date_format = re.compile(r'((\d{2})/(\d{2})/(\d{4}))')
date = str(input("Please enter the date to be checked: \n"))
matchObject = date_format.search(date)
day = int(matchObject.group(2))
month = int(matchObject.group(3))
year = int(matchObject.group(4))
truth_table = []
if (month>=1 and month<=12) and year>=1000 and year<=2999:
    truth_table.append(True)
else:
    truth_table.append(False)
if month == 4 or month == 6 or month == 8 or month == 11:
    if (day>=1) and (day<=30):
        truth_table.append(True)
    else:
        truth_table.append(False)
elif month == 2:
    if (day>=1) and (day<=28):
        truth_table.append(True)
    elif (day==29) and (year%4==0) and year%100==0 and year%400==0:
        truth_table.append(True)
    else:
        truth_table.append(False)
else:
    if (day>=1) and (day<=30):
        truth_table.append(True)
    else:
        truth_table.append(False)
if all(truth_table) == True:
    print("{}/{}/{} is a valid date.".format(matchObject.group(2),matchObject.group(3),matchObject.group(4)))
else:
    print("{}/{}/{} is not a valid date.".format(matchObject.group(2),matchObject.group(3),matchObject.group(4)))