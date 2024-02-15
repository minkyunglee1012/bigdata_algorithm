
import random

arr = [random.randint(1, 500) for _ in range(30)]
print(arr)

n = len(arr)


for i in range(1, n):
    for j in range(i, 0, -1):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
        else:
            break


print('오름차순')
print(arr)