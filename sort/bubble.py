


arr = [9, 5, 7, 1, 4, 6, 8]

n = len(arr)

for i in range(n):
    for j in range(0, n - 1 - i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]


print(arr)


