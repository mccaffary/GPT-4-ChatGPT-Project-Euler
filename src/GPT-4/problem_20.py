import math

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

factorial_100 = math.factorial(100)
result = sum_of_digits(factorial_100)

print(result)

