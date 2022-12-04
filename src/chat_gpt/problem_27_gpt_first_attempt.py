from sympy import isprime

# Set the maximum values for a and b
MAX_A = 1000
MAX_B = 1000

# Set the maximum number of primes found so far
max_primes = 0

# Set the product of the coefficients for the quadratic
# expression that produces the maximum number of primes
max_product = 0

# Iterate through values of a
for a in range(-MAX_A, MAX_A + 1):
    # Iterate through values of b
    for b in range(-MAX_B, MAX_B + 1):
        # Set the number of primes found for the current
        # values of a and b
        n_primes = 0
        # Set the value of n to 0
        n = 0
        # Loop until the quadratic expression is not prime
        while isprime(n**2 + (a*n) + b):
            # Increase the number of primes found
            n_primes += 1
            # Increase the value of n
            n += 1
        # Check if the number of primes found for the current
        # values of a and b is greater than the maximum number
        # of primes found so far
        if n_primes > max_primes:
            # Update the maximum number of primes found so far
            # far and the product of the coefficients for the quadratic
            # expression that produces the maximum number of primes
            max_primes = n_primes
            max_product = a * b

# Print the product of the coefficients for the quadratic
# expression that produces the maximum number of primes
print(max_product)

