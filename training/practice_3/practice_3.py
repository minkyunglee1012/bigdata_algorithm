# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq

import sys
sys.stdin = open("practice_3.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M, area)
    M_list = []
    # for k in range(M):
    # N*N 리스트에서 M * M으로 가능한 모든 리스트 만들자
    for i in range(N-M+1):
        for j in range(N-M+1):
            M_list.append([area[k+i][j:j+M] for k in range(M)])

    # print(M_list)

    # M * M 원소 각각의 합을 더해서 리스트 만들자
    M_sum_list = []
    for i in range(len(M_list)):
        a = 0
        for j in range(len(M_list[i])):
            a += sum(M_list[i][j])
        M_sum_list.append(a)
    # print(M_list)
    # print(M_sum_list)

    # 최대값을 구하는 것이므로 max
    res = max(M_sum_list)
    print(f"#{test_case} {res}")
    # for문 안 쪽에 코드를 작성해주세요

