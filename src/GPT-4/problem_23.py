def proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def is_abundant(n):
    return sum(proper_divisors(n)) > n

abundant_numbers = [n for n in range(12, 28123) if is_abundant(n)]
abundant_sums = set()

for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        abundant_sum = abundant_numbers[i] + abundant_numbers[j]
        if abundant_sum <= 28123:
            abundant_sums.add(abundant_sum)
        else:
            break

non_abundant_sums = set(range(1, 28124)) - abundant_sums
result = sum(non_abundant_sums)
print(result)

