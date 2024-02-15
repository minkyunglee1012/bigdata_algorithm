
# 인덱스를 써야함 # 값이 아니라 인덱스를 갱신..  -> 버블정렬보다 효율적

arr = [9, 5, 7, 1, 4, 8, 2]
n = len(arr)

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)