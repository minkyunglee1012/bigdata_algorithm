# testcase 1
# array = [1, 8, 3]  # [8, 1]

# testcase 2
array = [9, 10, 11, 8]  # [11, 2]


def solution(array):
    # 아래에 코드를 작성해주세요.
    answer = []
    answer.append(max(array))
    answer.append(min(array))
    return print(answer)


solution(array)