# testcase 1
# num_str = "123456789"  # 45

# testcase 2
num_str = "1000000"  # 1


def solution(num_str):
    answer = 0
    int_list = []
    num_list = list(num_str)
    for i in range(len(num_list)):
        int_list.append(int(num_list[i]))
    answer = sum(int_list)
    return answer


print(solution(num_str))
