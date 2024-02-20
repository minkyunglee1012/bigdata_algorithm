# testcase 1
# array = [7, 77, 17]  # 4

# testcase 2
# array = [10, 29]  # 0

array = [7, 77, 777, 70, 75]


def solution(array):
    return str(array).count('7')



# def solution(array):
#     str_array = []
#     for i in range(len(array)):
#         str_array.append(str(array[i]))
#
#     answer = 0
#     for j in range(len(str_array)):
#         for k in range(len(str_array[j])):
#             if str_array[j][k] == '7':
#                 answer += 1
#     return answer
#
print(solution(array))




# def solution(array):
#     answer = 0
#     for i in range(len(array)):
#         if ( array[i] - 7 ) % 10 == 0:
#             answer += 1
#     for i in range(len(array)):
#         if 1 <= (array[i] - 70) <= 9:
#             answer += 1
#     return answer


# print(solution(array))
