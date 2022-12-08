# Initialize a list of size 6,000,001 to store the primes
primes = [0] * 6000001

# Set the first two values to 0, since 0 and 1 are not prime
primes[0] = 0
primes[1] = 0

# Set all other values in the list to 1, since all numbers are prime until proven otherwise
for i in range(2, 6000001):
    primes[i] = 1

# Iterate through the list, setting all multiples of the current number to 0
# (i.e., marking them as not prime)
for i in range(2, 6000001):
    if primes[i] == 1:
        for j in range(i*2, 6000001, i):
            primes[j] = 0

# Sum all the values in the list that are prime
sum = 0
for i in range(2, 6000001):
    if primes[i] == 1:
        sum += i

# Print the sum of all prime numbers below six million
print(sum)

