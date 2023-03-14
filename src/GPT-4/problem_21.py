def proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def d(n):
    return sum(proper_divisors(n))

amicable_numbers = set()
for a in range(1, 10000):
    b = d(a)
    if a != b and d(b) == a:
        amicable_numbers.add(a)
        amicable_numbers.add(b)

result = sum(amicable_numbers)
print(result)

