import itertools

a = [1, 2, 3, 4]
print(list(itertools.combinations(a, 2)))
# 조합: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
print(list(itertools.permutations(a, 2)))
# 순열: [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
print(list(itertools.combinations_with_replacement(a, 2)))
# 중복조합: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
print(list(itertools.product(a, a)))
# 데카르트의 곱: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]

