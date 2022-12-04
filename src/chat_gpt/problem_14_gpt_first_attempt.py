# Function that returns the number of terms in the Collatz sequence starting at n
def collatz_sequence_length(n):
    # Initialize the length of the sequence to 1 (to account for the starting number n)
    length = 1

    # Generate the Collatz sequence
    while n > 1:
        # If n is even, divide it by 2
        if n % 2 == 0:
            n = n / 2
        # If n is odd, multiply it by 3 and add 1
        else:
            n = 3 * n + 1

        # Increment the length of the sequence
        length += 1

    # Return the length of the sequence
    return length

# Initialize the maximum length of a Collatz sequence to 0
max_length = 0

# Initialize the number that produces the maximum length of a Collatz sequence to 0
number_with_max_length = 0

# Iterate over all numbers between 1 and 1,000,000
for n in range(1, 1000000):
    # Calculate the length of the Collatz sequence starting at n
    length = collatz_sequence_length(n)

    # If the length of the sequence is greater than the maximum length, update the maximum length and the number with the maximum length
    if length > max_length:
        max_length = length
        number_with_max_length = n

# Print the number that produces the maximum length of a Collatz sequence
print(number_with_max_length)

