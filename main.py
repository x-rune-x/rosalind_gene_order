import math
from itertools import permutations


def get_permutations(n):
    integers = []
    for i in range(1, n+1):
        integers.append(i)

    perm = permutations(integers)
    for i in perm:
        print(i)


get_permutations(3)
