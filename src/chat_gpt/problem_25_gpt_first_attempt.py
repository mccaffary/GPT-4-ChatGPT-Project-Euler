def first_fibonacci_with_n_digits(n):
  if n == 1:
    return 1
  
  f1 = 1
  f2 = 1
  index = 2
  
  while len(str(f2)) < n:
    temp = f2
    f2 = f1 + f2
    f1 = temp
    index += 1
  
  return index

print(first_fibonacci_with_n_digits(1000))

