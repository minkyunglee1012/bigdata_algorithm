# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PnnU6AOsDFAUq

import sys
sys.stdin = open("practice_5.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    # print(arr)
    # 아래에 코드를 작성해주세요.
    # 월 별 일수를 딕셔너리에 저장하자
    month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    # 계산해야 할 월 수
    month = arr[2] - arr[0]

    # 첫 달은 총 일수에서 arr[1] 빼고 1더한 값
    first_res = month_days[arr[0]] - arr[1] + 1

    # 계산해야 할 월 수가 없으면 위 값 그대로 리턴
    if month == 0:
        res = first_res

    # 계산해야 할 월 수 딕셔너리 이용하여 구하고 마지막 달은 arr[3] 더하기
    else:
        for days in range(1, month):
            first_res += month_days[arr[0] + days]
        res = first_res + arr[3]
    #     arr[1]
    print(f"#{test_case} {res}")

"""
정답 
#1 31
#2 103
#3 161
#4 50
#5 120
#6 194
#7 81
#8 83
#9 238
#10 365
"""
