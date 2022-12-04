# Number of days in each month
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Number of Sundays that fell on the first of the month
num_sundays = 0

# Day of the week (0 = Sunday, 1 = Monday, etc.)
day_of_week = 1

# Loop over years in the 20th century
for year in range(1901, 2001):
    # Handle leap years
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28

    # Loop over months
    for month in range(12):
        # Check if the first of the month is a Sunday
        if day_of_week == 0:
            num_sundays += 1

        # Advance the day of the week
        day_of_week = (day_of_week + days_in_month[month]) % 7

