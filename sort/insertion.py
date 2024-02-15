

arr = [9, 5, 7, 1, 4]
n = len(arr)

# 0 인덱스에 해당하는 값을 정렬됨. (정렬된 영역)
# 정렬되지 않은 영역에 대해서 하나의 값을 선택하고,
# 정렬된 영역에 자기 자리를 찾아가야 한다.


for i in range(1, n):
    for j in range(i, 0, -1):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
        else:
            break

print(arr)