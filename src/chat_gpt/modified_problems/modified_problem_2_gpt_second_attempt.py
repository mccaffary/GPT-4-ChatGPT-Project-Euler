# define the first two terms of the Fibonacci sequence
a, b = 1, 2

# define the maximum value of the Fibonacci terms
max_value = 6000000

# initialize the sum of even-valued terms to 0
total = 0

# iterate over the Fibonacci sequence, adding up the even-valued terms
while b <= max_value:
    if b % 2 == 0:
        total += b
    a, b = b, a + b

# print the sum of even-valued terms
print(total)

