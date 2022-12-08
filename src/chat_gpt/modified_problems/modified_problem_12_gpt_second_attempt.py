# Function to check if a number is prime
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

# Function to find the prime factorization of a number
def prime_factorization(n):
  factors = []
  # Check for prime factors
  for i in range(2, n + 1):
    if is_prime(i):
      # Check if i is a factor of n
      while n % i == 0:
        factors.append(i)
        n = n / i
  return factors

# Function to find the number of factors of a number
# based on its prime factorization
def num_factors(n, prime_factors):
  factors = []
  for p in prime_factors:
    if p not in factors:
      factors.append(p)
  exponent_sum = 1
  for f in factors:
    exponent_sum *= (prime_factors.count(f) + 1)
  return exponent_sum

# Initialize variables
i = 1
triangle_number = 0
prime_factors = []

# Generate triangle numbers and find their prime factorizations
while True:
  triangle_number += i
  i += 1
  prime_factors += prime_factorization(i)
  num_factors = num_factors(triangle_number, prime_factors)
  # Check if the number of factors is greater than 1000
  if num_factors > 1000:
    print(triangle_number)
    break

