# 출처: https://swexpertacademy.com/main/learn/course/subjectDetail.do?subjectId=AWOVFCzaqeUDFAWg#
# 위 사이트에 들어간 후, 맨 아래에서 3번째에 위치한 1일차-전기버스 문제를 푸세요!!

import sys
sys.stdin = open("practice_2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = list(map(int, input().split(' ')))
    m_list = list(map(int, input().split(' ')))
    # print(K, N, M, m_list)
    # 충전 횟수와 현재 위치 변수 할당
    count = current = 0

    # 종점에 도착할 때까지 반복
    while current + K < N:
        # K 범위 안에서 현 위치를 조정하면서 이동
        for i in range(K, 0, -1):
            # 현재 위치 + 이동 거리만큼 이동했을 때 충전기가 있는 정류장일 경우
            if (current + i) in m_list:
                # 현재 위치 변경 및 충전 횟수 더하기
                current += i
                count += 1
                # for 문 종료
                break
        else:
            count = 0
            break




    print(f"#{test_case} {count}")
    # for문 안 쪽에 코드를 작성해주세요

