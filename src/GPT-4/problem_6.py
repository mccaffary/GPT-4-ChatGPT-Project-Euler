def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))

def square_of_sum(n):
    return sum(range(1, n + 1))**2

def difference(n):
    return square_of_sum(n) - sum_of_squares(n)

num = 100
result = difference(num)
print("The difference between the sum of the squares and the square of the sum of the first", num, "natural numbers is:", result)

