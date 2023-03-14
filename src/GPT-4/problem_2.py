def even_fibonacci_sum(limit):
    a, b = 1, 2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

limit = 4_000_000
result = even_fibonacci_sum(limit)
print("The sum of the even-valued Fibonacci terms not exceeding", limit, "is:", result)

