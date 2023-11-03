import itertools

n = int(input())
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
r = list(itertools.permutations(l, n))
print(len(r))