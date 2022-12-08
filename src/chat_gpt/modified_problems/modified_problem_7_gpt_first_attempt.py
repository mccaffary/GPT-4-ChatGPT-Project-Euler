# Start with a list of the first few primes
primes = [2, 3, 5, 7, 11, 13]

# The next number to check for primality
n = 15

# Keep generating primes until we have 13,001
while len(primes) < 13001:
    # Check if n is prime by checking if it's divisible by any of the primes we've already generated
    is_prime = True
    for p in primes:
        if n % p == 0:
            # If n is divisible by p, it's not prime
            is_prime = False
            break
    if is_prime:
        # If n is not divisible by any of the primes we've already generated, it's prime
        primes.append(n)
    # Increment n to check the next number
    n += 2

# Print the 13,001st prime
print(primes[-1])

