def sum_of_proper_divisors(n):
  sum = 0
  for i in range(1, n):
    if n % i == 0:
      sum += i
  return sum

def is_amicable_number(n):
  a = sum_of_proper_divisors(n)
  b = sum_of_proper_divisors(a)
  return n == b and a != b

def sum_of_amicable_numbers(n):
  sum = 0
  for i in range(1, n):
    if is_amicable_number(i):
      sum += i
  return sum

print(sum_of_amicable_numbers(10000))

