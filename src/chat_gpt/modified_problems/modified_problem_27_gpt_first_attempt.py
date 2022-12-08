# Import the isprime function from the sympy module
from sympy import isprime

# Define the function that finds the sum of the coefficients
# for the quadratic expression that produces the maximum
# number of primes
def find_coeff_sum():
    # Set the maximum number of primes found to 0
    max_primes = 0

    # Set the sum of the coefficients to 0
    coeff_sum = 0

    # Loop over the possible values of a
    for a in range(-999, 1000):
        # Loop over the possible values of b
        for b in range(-1000, 1001):
            # Set the number of primes found to 0
            primes = 0

            # Loop over the values of n
            for n in range(0, 1000):
                # Calculate the value of the quadratic expression
                q = n**2 + (a * n) + b

                # Check if the value is prime
                if isprime(q):
                    # Increment the number of primes found
                    primes += 1
                else:
                    # The value is not prime, so break the loop
                    break

            # Check if the number of primes found is greater than
            # the current maximum
            if primes > max_primes:
                # Set the maximum number of primes found to the
                # current number of primes found
                max_primes = primes

                # Set the sum of the coefficients to the current
                # values of a and b
                coeff_sum = a + b

    # Return the sum of the coefficients for the quadratic
    # expression that produces the maximum number of primes
    return coeff_sum

# Find the sum of the coefficients for the quadratic
# expression that produces the maximum number of primes
coeff_sum = find_coeff_sum()

# Print the result
print(coeff_sum)
