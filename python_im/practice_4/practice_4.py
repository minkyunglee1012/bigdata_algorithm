# testcase 1
# x, n = 2, 5  # [2, 4, 6, 8, 10]

# testcase 2
# x, n = 4, 3  # [4, 8, 12]

# testcase 3
x, n = -4, 2  # [-4, -8]


def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x * (i+1))
    return answer


print(solution(x,n))
