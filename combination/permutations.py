"""
combinations 코드를 기반으로 permutations 를 구현하라
순열(permutations) 는 [1, 2, 3, 4] 에서 2개의 순열을 구하라고 할 때, 아래와 같이 나온다.
[[1,2], [1,3], [1,4], [2,1], [2,3], [2,4], [3,1], [3,2], [3,4], [4,1], [4,2], [4,3]]

조합 코드를 기반으로 이해한 부분을 적용시키면 금방 해결할 수 있습니다.
떠오르지 않으면 조합을 천천히 이해하면서 코드로 구현해보세요.

순열을 구현했으면, 중복 조합과 데카르트 곱도 구현하세요.
"""


def perm(arr, n):
    result = []

    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        val = arr[i]
        rest_perm = perm(arr[:i] + arr[i+1:], n-1)
        for pm in rest_perm:
            result.append([val] + pm)

    return result


print('순열 :', perm([1, 2, 3, 4], 2))


def repeat_comb(arr, n):

    result = []

    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        val = arr[i]

        rest_repeat_comb = repeat_comb(arr[i:], n-1)
        for cb in rest_repeat_comb:
            result.append([val] + cb)

    return result


print('중복조합 : ', repeat_comb([1, 2, 3, 4], 2))


def product(arr, n):
    result = []

    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        val = arr[i]
        rest_prod = product(arr, n-1)
        for pd in rest_prod:
            result.append([val] + pd)

    return result


print('데카르트의 곱 :', product([1, 2, 3, 4], 2))