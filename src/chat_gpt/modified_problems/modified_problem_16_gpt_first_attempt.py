# Calculate 2**1500
result = 2 ** 1500

# Convert the result to a string and initialize the sum of the digits
result_str = str(result)
sum = 0

# Loop through the digits of the result and add each one to the sum
for digit in result_str:
  sum += int(digit)

# Print the sum of the digits
print(sum)

