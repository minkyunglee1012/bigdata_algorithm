
import random

arr_bubble = [random.randint(1, 500) for _ in range(30)]
arr_select = [random.randint(1, 500) for _ in range(30)]
arr_insert = [random.randint(1, 500) for _ in range(30)]

n = len(arr_bubble)

# bubble sort

print(arr_bubble)
for i in range(n):
    for j in range(n - i -1):
        if arr_bubble[j] > arr_bubble[j+1]:
            arr_bubble[j], arr_bubble[j+1] = arr_bubble[j+1], arr_bubble[j]

print(arr_bubble)


print('-'*150)


# selection sort

print(arr_select)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr_select[j] < arr_select[min_index]:
            min_index = j

    arr_select[i], arr_select[min_index] = arr_select[min_index], arr_select[i]

print(arr_select)


print('-'*150)

# insertion sort

print(arr_insert)
for i in range(1, n):
    for j in range(i, 0, -1):
        if arr_insert[j-1] > arr_insert[j]:
            arr_insert[j-1], arr_insert[j] = arr_insert[j], arr_insert[j-1]


print(arr_insert)
