def is_divisible(num):
    for i in range(1, 21):
        if num % i != 0:
            return False
    return True

num = 2520
while not is_divisible(num):
    num += 1
print(num)

