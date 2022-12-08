n = 500
sum_of_squares = (n * (n + 1) * (2 * n + 1)) / 6
sum = n * (n + 1) / 2
square_of_sum = sum ** 2
difference = sum_of_squares - square_of_sum

print(abs(difference))  # 15541225500

