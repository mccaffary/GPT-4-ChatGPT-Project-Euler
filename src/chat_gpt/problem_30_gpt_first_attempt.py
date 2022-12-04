# Initialize the sum
total_sum = 0

# Iterate over the numbers from 2 to 999999 (the upper limit is 999999 because
# 9**5 * 6 = 354294, so any number greater than that will definitely have a
# digit sum greater than itself)
for num in range(2, 999999):
  # Initialize the sum of the fifth powers of the digits
  digit_sum = 0
  
  # Convert the number to a string so we can iterate over its digits
  num_str = str(num)
  
  # Iterate over the digits in the number
  for digit in num_str:
    # Raise the digit to the fifth power and add it to the digit sum
    digit_sum += int(digit)**5
  
  # If the sum of the fifth powers of the digits is equal to the original number,
  # add it to the total sum
  if digit_sum == num:
    total_sum += num

# Print the final total sum
print(total_sum)

