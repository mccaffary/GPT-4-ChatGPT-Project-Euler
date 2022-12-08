# Function to return the day of the week (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
# for the first day of a given year
def first_day_of_year(year):
  # The day of the week for 1 Jan 1900 was a Monday (day 1)
  day = 1

  # Loop through the months of the year
  for month in range(1, 13):
    # Add the number of days in the month to the day of the week
    if month in [4, 6, 9, 11]:
      day += 30
    elif month == 2:
      if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        day += 29
      else:
        day += 28
    else:
      day += 31

    # If the day of the week is greater than 7, subtract 7
    if day > 7:
      day -= 7

  # Return the day of the week for the first day of the year
  return day

# Initialize the count of Sundays that fell on the first of the month
sundays = 0

# Loop through the years from 1901 to 2000 and check if the first day of the year
# is a Sunday (day 0)
for year in range(1901, 2001):
  if first_day_of_year(year) == 0:
    sundays += 1

# Print the count of Sundays that fell on the first of the month
print(sundays)

