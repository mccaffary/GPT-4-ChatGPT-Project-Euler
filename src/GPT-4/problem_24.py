import itertools

digits = '0123456789'
permutations = itertools.permutations(digits)

millionth_permutation = ''.join(next(itertools.islice(permutations, 999999, None)))
print(millionth_permutation)

