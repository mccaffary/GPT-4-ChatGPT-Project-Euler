def find_recurring_cycle(n):
    for t in range(1, n):
        if 1 == 10 ** t % n:
            return t
    return 0

longest = max(range(2, 1000), key=find_recurring_cycle)
print(longest)

