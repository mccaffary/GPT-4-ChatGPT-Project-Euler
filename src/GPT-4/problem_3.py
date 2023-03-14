def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(num):
    factor = 2
    while factor <= num:
        if num % factor == 0 and is_prime(factor):
            num //= factor
        else:
            factor += 1
    return factor

number = 600851475143
result = largest_prime_factor(number)
print("The largest prime factor of", number, "is:", result)

