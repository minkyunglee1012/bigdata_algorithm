
# 1. 배열에서 중간값을 선택
# 2. 중간값과 찾는 값을 비교하고 같지 않다면 3번, 같다면 탐색 종료
# 3. 찾는 값과 중간값을 비교해서 범위를 줄임
# 3.1 찾는 값 < 중간값인 경우, 찾고자 하는 범위를 중간값 왼쪽으로 좁힘
# 3.2 찾는 값 > 중간값인 경우, 찾고자 하는 범위를 중간값 오른쪽으로 좁힘
# 4. 좁힌 범위를 대상으로 1번 과정을 다시 반복

# 함수 선언부
def binary_search(arr, target):
    # 맨 왼쪽을 left, 맨 오른쪽을 right
    left = 0
    right = len(arr) - 1

    # left가 right를 넘지 않으면, 위의 1~4번 과정을 반복
    while left <= right:
        # 여기서 mid, left, right은 index를 의미
        # mid는 left와 right의 중간 위치를 의미
        mid = (left + right) // 2
        mid_value = arr[mid]

        # 중간값이 찾는값과 같다면, 바로 탐색 종료
        if mid_value == target:
            return mid
        # 중간값 < 찾는 값, 오른쪽으로 범위를 좁힘
        elif mid_value < target:
            left = mid + 1
        # 중간값 > 찾는 값, 왼쪽으로 범위를 좁힘
        else:
        # elif mid_value > target:
            right = mid - 1

    return -1


# 함수 실행
M, arr_1 = 9, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(arr_1, M)
print(result)