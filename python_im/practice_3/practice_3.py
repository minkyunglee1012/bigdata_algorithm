# testcase 1
# a, b = [1, 2, 3, 4] , [-3, -1, 0, 2]  # 3

# testcase 2
a, b = [-1, 0, 1] , [1, 0, -1]  # -2


def solution(a, b):
    dot_sum = 0
    for i in range(len(a)):
        dot_sum += a[i] * b[i]
    return dot_sum


print(solution(a, b))
