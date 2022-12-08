# Function to calculate the factorial of a given number and return the sum of the digits of the result
def factorial_sum(n):
  # Initialize the result to 1
  result = 1

  # Calculate the factorial by multiplying the numbers from 1 to n
  for i in range(1, n+1):
    result *= i

  # Convert the result to a string and initialize the sum of the digits
  result_str = str(result)
  sum = 0

  # Loop through the digits of the result and add each one to the sum
  for digit in result_str:
    sum += int(digit)

  # Return the sum of the digits
  return sum

# Print the sum of the digits in the number 200!
print(factorial_sum(200))

