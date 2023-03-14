def find_longest_recurring_cycle(limit):
    max_cycle_length = 0
    max_d = 0

    for d in range(2, limit):
        remainders = set()
        remainder = 1

        while remainder not in remainders and remainder != 0:
            remainders.add(remainder)
            remainder = (remainder * 10) % d

        cycle_length = len(remainders) if remainder != 0 else 0

        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            max_d = d

    return max_d


result = find_longest_recurring_cycle(1000)
print(result)

