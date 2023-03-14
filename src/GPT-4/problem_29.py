distinct_terms = set()

for a in range(2, 101):
    for b in range(2, 101):
        term = a ** b
        distinct_terms.add(term)

result = len(distinct_terms)
print(result)

