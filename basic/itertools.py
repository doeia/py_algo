# product, permutations, combinations, accumulate, groupby and infinite iterator
from itertools import product, permutations
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

c = [1, 2, 3]
perm = permutations(c)
print(list(perm))
