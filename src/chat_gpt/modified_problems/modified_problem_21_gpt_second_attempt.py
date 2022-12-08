# Function to return the sum of the proper divisors of a given number
def sum_proper_divisors(n):
  # Initialize the sum of the proper divisors to 0
  sum = 0

  # Loop through the numbers from 1 to n-1 and check if they are proper divisors
  # of n (i.e. they divide evenly into n and are less than n)
  for i in range(1, n):
    if n % i == 0:
      sum += i

  # Return the sum of the proper divisors
  return sum

# Initialize the sum of amicable numbers to 0
sum = 0

# Loop through the numbers from 1 to 20000 and check if they are amicable
for a in range(1, 20000):
  b = sum_proper_divisors(a)
  if a != b and sum_proper_divisors(b) == a:
    sum += a

# Print the sum of amicable numbers
print(sum)

