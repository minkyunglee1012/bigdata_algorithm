# 출처: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg#
# 위 사이트에 들어간 후, 맨 아래 1일차-구간합 문제를 푸세요!!

import sys
sys.stdin = open("practice_2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    # print(N, M, num_list)
    # for문 안 쪽에 코드를 작성해주세요
    sum_list = []
    for i in range(N-M+1):
        sum_list.append(sum(num_list[i:i+M]))

    res = max(sum_list) - min(sum_list)


    print(f"#{test_case} {res}")

