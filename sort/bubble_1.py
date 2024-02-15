'''
직접 코드로 버블 정렬 구현하기 (내림차순)
'''


array = [9, 5, 7, 1, 4]

n = len(array)

for i in range(n):
    for j in range(0, n - 1 - i):
        if array[j] < array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)

print('-'*150)

import random

array_1 = [random.randint(1, 1000) for _ in range(30)]

print(array_1)

for i in range(len(array_1)):
    for j in range(0, len(array_1) - 1 - i):
        if array_1[j] < array_1[j+1]:
            array_1[j], array_1[j+1] = array_1[j+1], array_1[j]

print('내림차순 ↓')
print(array_1)

for i in range(len(array_1)):
    for j in range(0, len(array_1) - 1 - i):
        if array_1[j] > array_1[j+1]:
            array_1[j], array_1[j+1] = array_1[j+1], array_1[j]

print('오름차순 ↓')
print(array_1)