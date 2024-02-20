# testcase 1
num_list = [4, 2, 6, 1, 7, 6]  # 17

# testcase 2
# num_list = [-1, 2, 5, 6, 3]  # 8

# 홀수 합 짝수 합 중 큰 값 반환
# 인덱스 주의

def solution(num_list):
    # 아래에 코드를 작성해주세요.
    odd_sum = 0
    even_sum = 0
    for i in range(len(num_list)):
        if i % 2 == 1:
            even_sum += num_list[i]
        else:
            odd_sum += num_list[i]

      # sol1
    # if even_sum > odd_sum:
    #     return even_sum
    # return odd_sum

     # sol2
    # return max(even_sum, odd_sum)

    #sol3
    return even_sum if even_sum > odd_sum else odd_sum



print(solution(num_list))

