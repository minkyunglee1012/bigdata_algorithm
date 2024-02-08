# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=4

import sys
sys.stdin = open("practice_3.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    farm_list = [list(map(int, input())) for _ in range(N)]
    # print(N, farm_list)
    # len(far_list) // 2와 len(far_list) - len(far_list)//2 나눠서 더하자
    if len(farm_list) == 1:
        res = farm_list[0][0]
    else:
        n_1 = len(farm_list) // 2

        # n_1 순회하면서 + i - i 만큼 더하기
        sum_1 = farm_list[0][n_1]
        for i in range(1, n_1 + 1):
            sum_1 += sum(farm_list[i][n_1 - i: n_1 + i + 1])

        # 나머지 부분 순회하면서 더하기
        sum_2 = farm_list[-1][n_1]
        i = n_1 - 1
        for j in range(n_1 + 1, len(farm_list) - 1):
            sum_2 += sum(farm_list[j][n_1 - i: n_1 + i + 1])
            i -= 1
        res = sum_1 + sum_2
    #
    # print(res)
    print(f"#{test_case} {res}")


    # for문 안 쪽에 코드를 작성해주세요
