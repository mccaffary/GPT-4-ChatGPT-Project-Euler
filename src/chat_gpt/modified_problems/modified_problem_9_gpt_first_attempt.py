# Import the square root function from the math module
from math import sqrt

# Function to check if a number is a perfect square
def is_perfect_square(n):
  return int(sqrt(n))**2 == n

# Function to find the Pythagorean triplet that sums to 1000
def pythagorean_triplet_with_sum(n):
  for a in range(1, n):
    for b in range(a + 1, n):
      c = n - a - b
      if a**2 + b**2 == c**2:
        return a, b, c

# Find the Pythagorean triplet that sums to 1000
a, b, c = pythagorean_triplet_with_sum(1000)

# Print the result of a**2 + (2*b) + c
print(a**2 + (2 * b) + c)

