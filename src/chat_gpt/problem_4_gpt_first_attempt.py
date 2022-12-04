# Initialize largest palindrome to 0
largest_palindrome = 0

# Loop through all possible pairs of 3-digit numbers
for i in range(100, 1000):
  for j in range(100, 1000):
    # Calculate the product of the two numbers
    product = i * j
    
    # Convert the product to a string
    product_str = str(product)
    
    # Check if the product is a palindrome (i.e. the string is the same forwards and backwards)
    is_palindrome = product_str == product_str[::-1]
    
    # If the product is a palindrome and is larger than the current largest, update the largest
    if is_palindrome and product > largest_palindrome:
      largest_palindrome = product

# Print the largest palindrome
print(largest_palindrome)

