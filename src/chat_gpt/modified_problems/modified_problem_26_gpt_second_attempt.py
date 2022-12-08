import decimal

# Function to return the length of the recurring cycle of 1/d
def recurring_cycle_length(d):
  # Use the decimal module to perform decimal division and get the decimal representation of 1/d as a string
  s = str(decimal.Decimal(1) / decimal.Decimal(d))[2:]

  # Search the string for the longest recurring sequence of digits and return the length of that sequence
  for i in range(len(s) // 2, 0, -1):
    if s[:i] == s[i:2 * i]:
      return i
  return 0

# Loop through all values of d < 2000 and find the one with the longest recurring cycle
max_length = 0
max_d = 0
for d in range(2, 2000):
  length = recurring_cycle_length(d)
  if length > max_length:
    max_length = length
    max_d = d

# Print the value of d for which 1/d has the longest recurring cycle
print(max_d)

