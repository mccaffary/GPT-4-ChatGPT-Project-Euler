def triangle_number(n):
    return n * (n + 1) // 2


def count_divisors(n):
    count = 0
    i = 1
    while i * i < n:
        if n % i == 0:
            count += 2
        i += 1
    if i * i == n:
        count += 1
    return count


def first_triangle_number_with_n_divisors(min_divisors):
    n = 1
    while True:
        triangle = triangle_number(n)
        divisors = count_divisors(triangle)
        if divisors > min_divisors:
            return triangle
        n += 1


result = first_triangle_number_with_n_divisors(500)
print(result)

