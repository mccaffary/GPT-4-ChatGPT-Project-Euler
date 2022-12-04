# Function to find the sum of the proper divisors of a number
def sum_proper_divisors(n):
    sum = 0
    # Loop over all numbers from 1 to n/2 (since n is always greater than the sum of its proper divisors)
    for i in range(1, n//2+1):
        # If i is a divisor of n, add it to the sum
        if n % i == 0:
            sum += i
    # Return the sum of the proper divisors
    return sum

# Function to check if a number is abundant
def is_abundant(n):
    # If the sum of the proper divisors of n is greater than n, return True (the number is abundant)
    if sum_proper_divisors(n) > n:
        return True
    # Otherwise, return False (the number is not abundant)
    return False

# Find all the abundant numbers less than 28123
abundant_numbers = []
for i in range(1, 28123):
    if is_abundant(i):
        abundant_numbers.append(i)

# Initialize the total sum of the numbers that cannot be written as the sum of two abundant numbers to 0
total_sum = 0

# Loop over all numbers from 1 to 28123
for i in range(1, 28123):
    # Initialize a flag to False
    flag = False
    # Loop over all abundant numbers in the list
    for j in abundant_numbers:
        # If the number is less than the current abundant number, break out of the loop
        if i < j:
            break
        # If the difference between the number and the current abundant number is in the list of abundant numbers,
        # set the flag to True and break out of the loop
        if i -

