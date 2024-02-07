"""
조합(combinations) 는 [1, 2, 3, 4] 에서 2개의 조합을 구하라고 할 때, 아래와 같이 나온다.
=> [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
"""


# 조합을 구하는 함수
def comb(arr, n):
    # 구한 조합을 저장할 변수
    result = []

    # 어떤 조건일 때, 어떻게 처리하면 되겠다!
    # 재귀 종료 조건
    if n == 1:
        # 코드 1
        # res = []
        # for i in arr:
        #     res.append([i])

        # 코드 2
        return [[i] for i in arr]

    # 재귀 구현
    # 주어진 리스트에 대해서 순회
    for i in range(len(arr)):
        val = arr[i]
        # 선택한 값의 이후 리스트들을 스스로에게 건네줌
        # 이 때, 선택 해야 하는 조합 수를 1개 줄여서 건네준다.
        rest_comb = comb(arr[i+1:], n-1)

        for cb in rest_comb:
            result.append([val] + cb)

    return result

print(comb([1, 2, 3, 4, 5], 3))


# def comb(arr, n):
#     result = []
#     if n == 1:
#         return [[i] for i in arr]
#
#     for i in range(len(arr)):
#         val = arr[i]
#
#         rest_comb = comb(arr[i+1:], n-1)
#
#         for cb in rest_comb:
#             result.append([val] + cb)
#
#     return result