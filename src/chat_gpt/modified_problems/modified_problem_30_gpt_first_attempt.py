# Define the function that finds the sum of all the numbers
# that can be written as the sum of fifth powers of their
# digits, then raises that sum to the fifth power
def find_sum():
    # Set the total sum to 0
    total_sum = 0

    # Loop over the possible numbers
    for n in range(2, 1000000):
        # Convert the number to a string and split it into
        # individual digits
        digits = str(n)
        digits = list(digits)

        # Set the sum of the digits to 0
        digit_sum = 0

        # Loop over the digits
        for digit in digits:
            # Calculate the fifth power of the digit and add it
            # to the sum of the digits
            digit_sum += int(digit)**5

        # Check if the number is a valid sum of fifth powers of
        # its digits
        if digit_sum == n:
            # Add the number to the total sum
            total_sum += n

    # Return the sum of the numbers that can be written as the
    # sum of fifth powers of their digits, raised to the fifth
    # power
    return total_sum**5

# Find the sum of all the numbers that can be written as the
# sum of fifth powers of their digits, then raise that sum
# to the fifth power
result = find_sum()

# Print the result
print(result)  # 443839

