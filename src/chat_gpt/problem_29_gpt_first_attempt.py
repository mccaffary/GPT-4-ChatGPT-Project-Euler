# Set the range of values for a and b
a_range = range(2, 101)
b_range = range(2, 101)

# Initialize an empty set to store the terms
terms = set()

# Loop through all values of a and b, compute a**b, and add it to the set
for a in a_range:
  for b in b_range:
    term = a**b
    terms.add(term)

# Sort the terms in numerical order
terms = sorted(terms)

# Print the number of distinct terms
print(len(terms))

