def sum_of_fifth_powers_of_digits(n):
    return sum(int(digit) ** 5 for digit in str(n))

upper_limit = 6 * (9 ** 5)  # 6 because 9**5 * 6 is the largest sum we need to consider
fifth_power_numbers = []

for num in range(10, upper_limit + 1):
    if num == sum_of_fifth_powers_of_digits(num):
        fifth_power_numbers.append(num)

result = sum(fifth_power_numbers)
print(result)

