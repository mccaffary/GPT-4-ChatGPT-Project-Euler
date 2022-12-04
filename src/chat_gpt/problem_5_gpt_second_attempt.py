# Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

numbers = list(range(1, 21)) # create a list of the numbers from 1 to 20
smallest = 1 # initialize the smallest number to 1

for num in numbers:
    smallest *= num # multiply the smallest number by each number in the list

print(smallest) # print the result

