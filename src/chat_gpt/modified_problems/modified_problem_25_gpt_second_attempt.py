# Function to return the index of the first term in the Fibonacci sequence to contain 2000 digits

import itertools

def first_fibonacci_2000_digits():
  # Initialize the variables a and b to 1 and 1 respectively
  a = 1
  b = 1

  # Loop from 3 to infinity
  for i in itertools.count(3):
    # Add a and b and check if the result has 2000 digits
    c = a + b
    if len(str(c)) == 2000:
      # Return the current loop index if the result has 2000 digits
      return i

    # Update a and b with the result and the previous value of a respectively
    a = b
    b = c

# Print the index of the first term in the Fibonacci sequence to contain 2000 digits
print(first_fibonacci_2000_digits())

