from math import sqrt

def num_divisors(n):
  # Keep track of how many times we've seen each prime factor of n
  prime_factors = {}

  # Check for each prime number up to the square root of n
  for i in range(2, int(sqrt(n)) + 1):
    # Divide out the prime number as many times as possible
    while n % i == 0:
      n /= i
      # If we've seen this prime factor before, increment its count
      if i in prime_factors:
        prime_factors[i] += 1
      # Otherwise, set its count to 1
      else:
        prime_factors[i] = 1

  # If n is greater than 1 after dividing out the prime factors,
  # then it must be prime. In this case, add it to the prime_factors
  # dictionary with a count of 1.
  if n > 1:
    prime_factors[n] = 1

  # The number of divisors is the product of (prime_factor[i] + 1) for all
  # i in the prime_factors dictionary.
  num_divisors = 1
  for key in prime_factors:
    num_divisors *= (prime_factors[key] + 1)

  return num_divisors

# Start with the first triangle number (1)
triangle_number = 1
n = 2
# Keep track of the number of divisors of the current triangle number
num_divisors = 1
# Continue until we find a triangle number with over 1000 divisors
while num_divisors <= 1000:
  # Compute the next triangle number by adding the next natural number
  triangle_number += n
  # Increment n to get the next natural number
  n += 1
  # Compute the number of divisors of the current triangle number
  num_divisors = num_divisors(triangle_number)

# Print the result
print(triangle_number)

