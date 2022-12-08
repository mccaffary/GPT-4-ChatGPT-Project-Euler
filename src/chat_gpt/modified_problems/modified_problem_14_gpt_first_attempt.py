# Function to generate the Collatz sequence for a given number
def collatz(n):
  sequence = [n]
  while n != 1:
    if n % 2 == 0:
      n = n // 2
    else:
      n = 3 * n + 1
    sequence.append(n)
  return sequence

# Initialize variables
max_length = 0
max_start = 0

# Generate the Collatz sequence for each number from 1 to 2 million
# and keep track of the length of each sequence
for i in range(1, 2000001):
  sequence = collatz(i)
  length = len(sequence)
  if length > max_length:
    max_length = length
    max_start = i

# Print the starting number that produces the longest sequence
print(max_start)

