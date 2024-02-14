# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh

import sys
sys.stdin = open("practice_1.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # for문 안 쪽에 코드를 작성해주세요
    # 아래 ans는 자유롭게 바꾼 후 정답을 출력하세요.
    ans = 0
    row_list = []
    col_list = []
    cross_list = []
    cross_sum = 0
    cross_sum2 = 0

    for i in range(100):
        row_list.append(sum(arr[i]))
        cross_sum += arr[i][i]
        cross_sum2 += arr[i][len(arr) - i - 1]
        col_sum = 0
        for j in range(100):
            col_sum += arr[j][i]
        col_list.append(col_sum)
    # print(col_list)

    cross_list.append(cross_sum)
    cross_list.append(cross_sum2)

    # print(cross_sum, cross_sum2)

    ans = max(max(row_list), max(col_list), max(cross_list))


    print(f"#{tc} {ans}")

