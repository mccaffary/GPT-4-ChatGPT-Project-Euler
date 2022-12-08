# Function to check if a year is a leap year
def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# Function to get the number of days in a month
def days_in_month(month, year):
  if month in [4, 6, 9, 11]:
    return 30  # April, June, September, and November have 30 days
  elif month == 2:
    if is_leap_year(year):
      return 29  # February has 29 days in a leap year
    else:
      return 28  # February has 28 days in a non-leap year
  else:
    return 31  # All other months have 31 days

# Initialize variables
year = 1900  # Start at the year 1900
month = 1  # Start at the month of January
day = 1  # Start on the first day of the month
day_of_week = 1  # Start on Monday (day 1)
sundays_on_first = 0  # Number of Sundays on the first of the month

# Loop through the years, months, and days
while year < 2001:
  # Get the number of days in the current month
  days = days_in_month(month, year)

  # Loop through the days of the current month
  for i in range(1, days + 1):
    # If the day is the first of the month

