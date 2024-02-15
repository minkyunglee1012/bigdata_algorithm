# testcase 1
M, arr_1 = 9, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 8

# testcase 2
# M, arr_1 = 7, [1, 2, 3, 4, 5, 6, 8, 9, 10]  # -1

# 아래에 코드를 작성하세요.

def solution(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid

        elif mid_value < target:
            left = mid + 1

        elif mid_value > target:
            right = mid -1

    return -1


print(solution(arr_1, M))