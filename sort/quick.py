
def quick_sort(arr, left, right):
    # 왼쪽 시작지점과 오른쪽 시작지점이 같거나 왼쪽이 더 큰 경우 정렬 종료
    # 일반적으로 계속 쪼개지다보면 left 와 right가 만나게 됨.
    # len(list) = 1 인 경우에도 left == right
    if left >= right:
        return

    # 피벗을 기준으로 왼쪽에는 피벗보다 작은값, 오른쪽에는 피벗보다 큰 값으로 정렬하는 과정
    mid = partition(arr, left, right)
    # 피벗을 기준으로 정렬 후에 다시 피벗 왼쪽 리스트에 대해서 정렬
    quick_sort(arr, left, mid - 1)
    # 피벗을 기준으로 정렬 후에 다시 피벗 오른쪽 리스트에 대해서 정렬
    quick_sort(arr, mid, right)


# 피벗을 기준으로 왼쪽에는 피벗보다 작은 값, 오른쪽에는 피벗보다 큰 값을 정렬하는 함수
def partition(arr, left, right):
    # 피벗은 배열의 가운데 값으로 설정
    pivot = arr[(left + right) // 2]

    # 리스트의 왼쪽 포인트와 오른쪽 포인트가 교차하지 않는다면,
    # 아래 값 교환 과정을 계속해서 반복
    while left <= right:
        # 왼쪽 포인트 값이 피벗보다 크거나 같을때까지 왼쪽 포인트의 위치를 오른쪽으로 이동
        while arr[left] < pivot:
            left += 1
        # 오른쪽 포인트 값이 피벗보다 작거나 같을때까지 오른쪽 포인트의 위치를 왼쪽으로 이동
        while arr[right] > pivot:
            right -= 1
        # 두 포인트 값이 교차하지 않았다면, 두 값을 교환
        # 교환 후에 왼쪽 포인트는 오른쪽으로 1, 오른쪽 포인트는 왼쪽으로 1 이동시킴
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # left 좌표를 기준으로 왼쪽, 오른쪽 리스트를 나뉘어서 다시 퀵 정렬 진행
    return left


def main():
    arr = [3, 1, 7, 4, 5, 1, 8, 2]
    quick_sort(arr, 0, len(arr) - 1)   # 인덱스이기 때문에 len(arr)-1
    for a in arr:
        print(a, end=" ")

main()







# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             lesser_arr.append(num)
#         elif num > pivot:
#             greater_arr.append(num)
#         else:
#             equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
