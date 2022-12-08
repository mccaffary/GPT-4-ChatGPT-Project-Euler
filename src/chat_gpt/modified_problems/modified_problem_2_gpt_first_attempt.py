fib_nums = [1, 2]  # Initialize the list of Fibonacci numbers
fib_sum = 0  # Initialize the sum of the even Fibonacci numbers

# Iterate through the Fibonacci numbers until we reach 6 million
while fib_nums[-1] <= 6000000:
  # Calculate the next Fibonacci number in the sequence
  next_num = fib_nums[-1] + fib_nums[-2]
  fib_nums.append(next_num)
  
  # If the new number is even, add it to the sum
  if next_num % 2 == 0:
    fib_sum += next_num
    
# Print the sum of the even Fibonacci numbers
print(fib_sum)

