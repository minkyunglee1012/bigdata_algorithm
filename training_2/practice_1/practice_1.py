# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBnA2jaxDsDFAWr

import sys
sys.stdin = open("practice_1.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    scores = list(map(int, input().split()))
    # print(scores)

    score_sum = 0
    for i in range(len(scores)):
        if scores[i] < 40:
            score_sum += 40
        else:
            score_sum += scores[i]

    ans = int(score_sum / 5)

    print(f'#{test_case} {ans}')