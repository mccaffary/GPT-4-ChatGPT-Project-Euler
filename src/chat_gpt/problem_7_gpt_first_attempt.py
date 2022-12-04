def is_prime(n):
    # Check if n is a prime number
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    # Find the nth prime number
    prime_count = 0
    num = 1
    while prime_count < n:
        num += 1
        if is_prime(num):
            prime_count += 1
    return num

# Find the 10,001st prime number
n = 10001
#print(f"The {n}th prime number is {nth_prime(n)}.")
print(nth_prime(n))

