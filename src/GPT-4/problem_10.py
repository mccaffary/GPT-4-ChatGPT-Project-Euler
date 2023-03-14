def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for num, is_prime in enumerate(primes):
        if is_prime:
            yield num
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False

limit = 2_000_000
primes = list(sieve_of_eratosthenes(limit))
prime_sum = sum(primes)

print(f"The sum of all the primes below {limit} is: {prime_sum}")

