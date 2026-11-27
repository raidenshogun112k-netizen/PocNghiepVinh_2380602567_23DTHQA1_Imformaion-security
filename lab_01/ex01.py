import itertools

numbers = [1, 2, 3]

permutations = itertools.permutations(numbers)

for p in permutations:
    print(p)