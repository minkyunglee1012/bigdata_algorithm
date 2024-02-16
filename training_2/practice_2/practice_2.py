# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AX6PP9G6p1sDFAS9

import sys
sys.stdin = open("practice_2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(input())
    # print(arr)

    count = 0

    # for문 돌면서 x가 8번 이상이면 NO
    for i in range(len(arr)):
        if arr[i] == 'x':
            count += 1

    if count >= 8:
        ans = 'NO'

    else:
        ans = 'YES'

    print(f'#{test_case} {ans}')