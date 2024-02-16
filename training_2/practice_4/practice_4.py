# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh
import sys
sys.stdin = open("practice_4.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)

    while N > 0:
        arr[arr.index(max(arr))] = max(arr) - 1
        arr[arr.index(min(arr))] = min(arr) + 1
        N -= 1

    ans = max(arr) - min(arr)

    print(f'#{test_case} {ans}')
