def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

power_of_two = 2**1000
result = sum_of_digits(power_of_two)

print(result)

