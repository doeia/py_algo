# product, permutations, combinations, accumulate, groupby and infinite iterator
from itertools import combinations
from itertools import product, permutations
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print('prod', list(prod))

c = [1, 2, 3]
perm = permutations(c)
print('prod', list(perm))


# Example list
d = [1, 2, 3, 4]

# Generate all combinations of length 2
comb = combinations(d, 2)
print('comb', list(comb))

# Generate all combinations of length 3
comb = combinations(d, 3)
print('comb', list(comb))
