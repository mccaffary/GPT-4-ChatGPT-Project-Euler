def diagonal_sum_in_spiral(spiral_size):
    diagonal_sum = 1
    current_number = 1
    step = 2

    while step < spiral_size:
        for _ in range(4):
            current_number += step
            diagonal_sum += current_number
        step += 2

    return diagonal_sum

result = diagonal_sum_in_spiral(1001)
print(result)

