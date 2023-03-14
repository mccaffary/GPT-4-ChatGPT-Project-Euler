import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def smallest_multiple(n):
    multiple = 1
    for i in range(2, n + 1):
        multiple = lcm(multiple, i)
    return multiple

num = 20
result = smallest_multiple(num)
print("The smallest positive number that is evenly divisible by all of the numbers from 1 to", num, "is:", result)

