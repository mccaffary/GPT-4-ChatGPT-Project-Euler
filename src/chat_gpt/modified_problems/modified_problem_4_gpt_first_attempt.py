# Start with the largest 4-digit number and work our way down
for i in range(9999, 999, -1):
  for j in range(i, 999, -1):
    # Compute the product of the two numbers
    product = i * j

    # Convert the product to a string
    product_str = str(product)

    # Check if the string is a palindrome
    if product_str == product_str[::-1]:
      # We found a palindrome, print it and stop
      print(product)
      break

