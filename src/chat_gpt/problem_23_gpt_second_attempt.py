def is_abundant(n):
    divisors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    if sum(divisors) > n:
        return True
    return False

abundant_numbers = []
for i in range(1, 28124):
    if is_abundant(i):
        abundant_numbers.append(i)

abundant_sums = set()
for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        abundant_sums.add(abundant_numbers[i] + abundant_numbers[j])

print(sum(set(range(1, 28124)) - abundant_sums))

