# Function to generate all the permutations of a given list of numbers in lexicographic order
def permute(nums):
  # If the list has only one element, return the list
  if len(nums) == 1:
    return [nums]

  # Initialize the list of permutations
  perms = []

  # Loop through the numbers in the list
  for i, num in enumerate(nums):
    # Create a new list with the numbers from the original list except the current number
    other_nums = nums[:i] + nums[i+1:]

    # Generate all the permutations of the new list and add the current number to the beginning
    # of each permutation
    for perm in permute(other_nums):

