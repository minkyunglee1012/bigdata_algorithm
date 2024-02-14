# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWZ2IErKCwUDFAUQ
import sys
sys.stdin = open("practice_3.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    # 조합을 이용해서 숫자를 3개씩 나열하는 리스트 만든 후 각각의 합을 구하는 리스트를 만들자


    def combination(array, n):
        result = []
        if n == 1:
            return [[i] for i in array]

        for i in range(len(array)):
            val = array[i]
            rest_comb = combination(array[i+1:], n-1)
            for cb in rest_comb:
                result.append([val] + cb)

        return result

    comb_list = combination(arr, 3)

    com_sum = []
    for i in range(len(comb_list)):
        com_sum.append(sum(comb_list[i]))
    com_sum = list(set(com_sum))

    for i in range(4):
        com_sum.remove(max(com_sum))

    ans = max(com_sum)
    print(f"#{test_case} {ans}")
