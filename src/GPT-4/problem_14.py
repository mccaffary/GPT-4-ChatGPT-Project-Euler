def collatz_sequence_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def find_longest_collatz_sequence(limit):
    max_length = 0
    max_starting_number = 0
    for i in range(1, limit):
        current_length = collatz_sequence_length(i)
        if current_length > max_length:
            max_length = current_length
            max_starting_number = i
    return max_starting_number

longest_chain_start = find_longest_collatz_sequence(1000000)
print(longest_chain_start)

