def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def count_sundays_on_first_of_month(start_year, end_year):
    day_of_week = 1  # 1 Jan 1900 was a Monday
    sundays_on_first_of_month = 0

    # Calculate the day of the week for 1 Jan 1901
    for year in range(1900, start_year):
        for month in range(1, 13):
            day_of_week = (day_of_week + days_in_month(month, year)) % 7

    # Count Sundays on the first of the month between start_year and end_year
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if day_of_week == 0:  # Sunday
                sundays_on_first_of_month += 1
            day_of_week = (day_of_week + days_in_month(month, year)) % 7

    return sundays_on_first_of_month

sundays_on_first_of_month_20th_century = count_sundays_on_first_of_month(1901, 2000)
print(sundays_on_first_of_month_20th_century)

