import math

# Create a list of the numbers from 1 to 30
numbers = list(range(1, 31))

# Find the least common multiple of the numbers
lcm = math.lcm(*numbers)

# Print the result
print(lcm)

