def sum_of_multiples(limit):
    total = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

limit = 1000
result = sum_of_multiples(limit)
print("The sum of all the multiples of 3 or 5 below", limit, "is:", result)

