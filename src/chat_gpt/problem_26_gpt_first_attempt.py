max_cycle_length = 0
max_cycle_d = 0

for d in range(2, 1000):
  # Calculate the decimal representation of 1/d
  decimal = 1 / d
  
  # Convert the decimal to a string
  decimal_str = str(decimal)

  # Find the index of the decimal point in the string
  decimal_point_index = decimal_str.index('.')

  # Remove the decimal point from the string
  decimal_str = decimal_str[decimal_point_index + 1:]

  # Check if the decimal has a repeating pattern
  if '(' in decimal_str:
    # Find the start and end index of the repeating pattern
    pattern_start_index = decimal_str.index('(')
    pattern_end_index = decimal_str.index(')')

    # Calculate the length of the repeating pattern
    pattern_length = pattern_end_index - pattern_start_index - 1

    # Check if this is the longest repeating pattern we've seen so far
    if pattern_length > max_cycle_length:
      max_cycle_length = pattern_length
      max_cycle_d = d

# Print the value of d with the longest repeating pattern
print(max_cycle_d)

