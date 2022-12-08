largest_palindrome = 0

# Iterate over all possible pairs of 4-digit numbers
for i in range(1000, 10000):
    for j in range(1000, 10000):
        # Calculate the product of the two numbers
        product = i * j
        
        # Convert the product to a string
        product_str = str(product)
        
        # Check if the product is a palindrome
        is_palindrome = True
        for k in range(len(product_str) // 2):
            if product_str[k] != product_str[-k - 1]:
                is_palindrome = False
                break
        
        # If the product is a palindrome and larger than the previous largest palindrome, update our answer
        if is_palindrome and product > largest_palindrome:
            largest_palindrome = product

# Print the largest palindrome
print(largest_palindrome)

