def find_triplet():
    # Iterate over all possible values of a, b, and c
    for a in range(1, 1000):
        for b in range(a+1, 1000):
            for c in range(b+1, 1000):
                # Check if a, b, and c satisfy the conditions
                if a**2 + b**2 == c**2 and a + b + c == 1000:
                    # Return the product abc
                    return a * b * c

# Test the function
print(find_triplet())  # Expected output: 31875000

