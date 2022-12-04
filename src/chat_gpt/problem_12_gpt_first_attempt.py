from math import sqrt

def count_divisors(n):
    if n == 1:
        return 1
    divisor_count = 0
    sqrt_n = int(sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisor_count += 2
    if sqrt_n * sqrt_n == n:
        divisor_count -= 1
    return divisor_count

triangle_number = 0
for i in range(1, 1000000):
    triangle_number += i
    divisor_count = count_divisors(triangle_number)
    if divisor_count > 500:
        print(triangle_number)
        break

