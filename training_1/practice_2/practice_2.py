# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVWgkP6sQ0DFAUO

import sys
sys.stdin = open("practice_2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str_list = [[x for x in input()] for _ in range(5)]
    # for문 안 쪽에 코드를 작성해주세요
    # print(str_list)
    result = ''
    for j in range(15):
        for i in range(5):
            try:
                result += str_list[i][j]

            except:
                result += ''

    print(f"#{test_case} {result}")





