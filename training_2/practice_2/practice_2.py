# 출처: https://swexpertacademy.com/main/learn/course/subjectDetail.do?subjectId=AWOVFCzaqeUDFAWg#
# 위 사이트에 들어간 후, 맨 아래에서 3번째에 위치한 1일차-전기버스 문제를 푸세요!!

import sys
sys.stdin = open("practice_2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = list(map(int, input().split(' ')))
    m_list = list(map(int, input().split(' ')))
    print(K, N, M, m_list)
    # for문 안 쪽에 코드를 작성해주세요

