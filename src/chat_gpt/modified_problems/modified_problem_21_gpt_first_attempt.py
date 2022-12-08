# Function to calculate the sum of the proper divisors of a given number
def sum_proper_divisors(n):
  # Initialize the sum of the proper divisors to 0
  sum = 0

  # Loop through the numbers from 1 to n-1 and add the numbers that are divisors of n
  for i in range(1, n):
    if n % i == 0:
      sum += i

  # Return the sum of the proper divisors
  return sum

# Initialize the total sum of amicable numbers
total_sum = 0

# Loop through the numbers from 1 to 20000 and check if the sum of the proper divisors
# of each number is equal to a different number
for a in range(1, 20000):
  b = sum_proper_divisors(a)
  if b != a and sum_proper_divisors(b) == a:
    total_sum += a + b

# Print the total sum of amicable numbers
print(total_sum)

