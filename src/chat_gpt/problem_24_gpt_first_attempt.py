import itertools

permutations = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
millionth_permutation = permutations[1000000 - 1]

# Convert the tuple to a string and remove the comma and space characters
millionth_permutation_str = str(millionth_permutation).replace(',','').replace(' ','')

def remove_first_last_characters(string):
  return string[1:-1]


# Print the millionth permutation as a string
print(remove_first_last_characters(millionth_permutation_str))

