# Function to return the length of the recurring cycle in the decimal representation of 1/d
def recurring_cycle_length(d):
  # Initialize the variables remainders and remainder to an empty list and 10 respectively
  remainders = []
  remainder = 10

  # Loop until remainder is 0 or remainder is already in remainders
  for i in itertools.count():
    # Multiply remainder by 10, divide it by d, and append the remainder to remainders
    remainder = remainder * 10 % d
    if remainder == 0:
      # Return 0 if remainder is 0
      return 0
    if remainder in remainders:
      # Return the length of the recurring cycle if remainder is already in remainders
      return i - remainders.index(remainder)

    remainders.append(remainder)

# Initialize the variable max_

