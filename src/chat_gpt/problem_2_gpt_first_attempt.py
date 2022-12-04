# Start with the first two numbers in the sequence
fib1 = 1
fib2 = 2

# Keep track of the sum of the even-valued terms
sum = 0

# Loop until we reach a number greater than 4 million
while fib2 <= 4000000:
  # If the current number is even, add it to the sum
  if fib2 % 2 == 0:
    sum += fib2
  # Compute the next number in the sequence
  fib1, fib2 = fib2, fib1 + fib2

# Print the final sum
print(sum)

