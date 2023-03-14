def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_max_primes_quadratic(limit):
    max_count = 0
    max_a = 0
    max_b = 0

    for a in range(-limit + 1, limit):
        for b in range(-limit + 1, limit):
            n = 0
            while is_prime(n**2 + a * n + b):
                n += 1

            if n > max_count:
                max_count = n
                max_a = a
                max_b = b

    return max_a * max_b

result = find_max_primes_quadratic(1000)
print(result)

