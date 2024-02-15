# 반으로 분할하고, 합치는 함수 -> 실질적인 병합 정렬 함수

def merge_sort(arr):
    n = len(arr)
    # 재귀함수의 탈출 조건
    # 병합정렬은 1개가 될 때까지 반복해서 반으로 쪼개기 때문에
    if n <= 1:
        return arr

    mid = n // 2  # 리스트의 반 index
    left_half = arr[:mid]  # 반을 기준으로 왼쪽 리스트
    right_half = arr[mid:]  # 반을 기준으로 오른쪽 리스트

    left_half = merge_sort(left_half)  # 왼쪽 리스트에 대해서 다시 분할
    right_half = merge_sort(right_half)  # 오른쪽 리스트에 대해서 다시 분할

    return merge(left_half, right_half)  # 쪼개진 리스트에 대해서 정렬하면서 합치기


# 쪼개진 인자들을 정렬하면서 합치는 함수
def merge(left, right):
    # 정렬할 때 필요한 임시 저장 공간
    result = []

    # 합쳐야 하는 왼/오 리스트에 인자가 들어있는 경우 반복
    # 왼/오 리스트 중 인자가 하나도 들어있지 않은 경우에는 탈출
    while left and right:
        # 왼/오 리스트의 첫 번째 인자를 비교하고, 더 작은 값을 임시 저장공간에 저장
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # 왼/오 리스트에 남아 있는 인자들을 임시 저장공간에 저장
    result.extend(left)
    result.extend(right)

    # 병합된 리스트(임시저장공간)을 반환
    return result