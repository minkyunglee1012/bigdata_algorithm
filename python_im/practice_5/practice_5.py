# testcase 1
# a, b = 3, 5  # 34

# testcase 2
# a, b = 6, 1  # 14

# testcase 3
a, b = 2, 4  # 2


def solution(a, b):
    answer = 0
    if a % 2 == 1 and b % 2 == 1:
        answer += (a ** 2) + (b ** 2)
    elif a % 2 == 1 or b % 2 == 1:
        answer += 2 * (a + b)
    else:
        answer += abs(a-b)
    return answer


print(solution(a, b))
