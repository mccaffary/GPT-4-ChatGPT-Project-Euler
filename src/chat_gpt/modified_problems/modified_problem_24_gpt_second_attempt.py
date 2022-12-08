# Function to return the next lexicographic permutation of a given list of numbers
def next_permutation(nums):
  # Find the first element from the right that is smaller than the element to its right
  i = len(nums) - 2
  while i >= 0 and nums[i] >= nums[i+1]:
    i -= 1

  # If no such element was found, return the sorted list (this is the last permutation)
  if i < 0:
    return sorted(nums)

  # Find the smallest element to the right of the element found above that is greater than it
  j = len(nums) - 1
  while nums[j] <= nums[i]:
    j -= 1

  # Swap the elements found above
  num

