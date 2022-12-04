#!/bin/python

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31

def next_day(year, month, day):
    if day < days_in_month(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

# Start on a Monday in 1900, which was a leap year
year, month, day = 1900, 1, 1
day_of_week = 1

sunday_count = 0
while year < 2001:
    year, month, day = next_day(year, month, day)
    day_of_week = (day_of_week + 1) % 7
    if day_of_week == 0 and day == 1 and year >= 1901:
        sunday_count += 1

print(sunday_count)

