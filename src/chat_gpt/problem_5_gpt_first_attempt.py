import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
product = 1
for number in numbers:
    product *= number
gcd = math.gcd(numbers)
lcm = product // gcd
print(lcm)  # 232792560

