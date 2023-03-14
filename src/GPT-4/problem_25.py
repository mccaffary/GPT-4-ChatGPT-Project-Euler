def fibonacci_index_with_digits(digits_count):
    fib_a, fib_b = 1, 1
    index = 2
    
    while len(str(fib_b)) < digits_count:
        fib_a, fib_b = fib_b, fib_a + fib_b
        index += 1
    
    return index

result = fibonacci_index_with_digits(1000)
print(result)

