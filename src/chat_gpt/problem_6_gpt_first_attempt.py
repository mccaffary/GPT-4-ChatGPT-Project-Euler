n = 100

# compute the sum of the squares
sum_of_squares = 0
for i in range(1, n+1):
    sum_of_squares += i**2

# compute the square of the sum
square_of_sum = (n*(n+1)//2)**2

# compute the difference
difference = square_of_sum - sum_of_squares

# print the result
print(difference)

