# Function to return True if a given number is abundant and False otherwise
def is_abundant(n):
  # Initialize the sum of the proper divisors to 0
  sum = 0

  # Loop through the numbers from 1 to n-1 and check if they are proper divisors
  # of n (i.e. they divide evenly into n and are less than n)
  for i in range(1, n):
    if n % i == 0:
      sum += i

  # Return True if the sum of the proper divisors is greater than n and False otherwise
  return sum > n

# Initialize the list of abundant numbers and the sum of numbers that cannot be
# written as the sum of two abundant numbers
abund

