

import random

arr = [random.randint(1, 500) for _ in range(30)]
print(arr)
n = len(arr)


for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]


print('오름차순')
print(arr)


