# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Find the sum of all the primes below two million
limit = 2*10**6
sum = 0
for i in range(2, limit):
    if is_prime(i):
        sum += i
print(sum)

