# testcase 1
# type, M, arr_1 = "RIGHT", 3, [1, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10]  # 5

# testcase 2
# type, M, arr_1 = "RIGHT", 7, [1, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10]  # -1
#
# # 아래에 코드를 작성하세요.
type, M, arr_1 = "LEFT", 3, [1, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10]  # 3

# 아래에 코드를 작성하세요.


def solution(arr, target, type):
    left = 0
    right = len(arr) -1
    res = -1

    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]

        # 값을 찾아도 탐색을 중단하지 않고,
        # 값을 찾는 타입에 따라서
        # 다시 범위를 좁혀서 같은 값을 탐색한다.
        if mid_value == target:
            res = mid
            if type == 'RIGHT':
                left = mid + 1
            elif type == 'LEFT':
                right = mid - 1

        elif mid_value < target:
           left = mid + 1

        elif mid_value > target:
           right = mid - 1

    return res


print(solution(arr_1, M, type))


