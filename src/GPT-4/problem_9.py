def find_pythagorean_triplet(target_sum):
    for a in range(1, target_sum):
        for b in range(a + 1, target_sum - a):
            c = target_sum - a - b
            if a**2 + b**2 == c**2:
                return a, b, c
    return None, None, None

target_sum = 1000
a, b, c = find_pythagorean_triplet(target_sum)

if a and b and c:
    product = a * b * c
    print(f"The Pythagorean triplet for which a + b + c = {target_sum} is ({a}, {b}, {c}).")
    print(f"The product abc is: {product}")
else:
    print(f"No Pythagorean triplet found for the target sum {target_sum}.")

