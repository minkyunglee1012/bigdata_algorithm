# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14jJh6ACYCFAYD
import sys
sys.stdin = open("practice_3.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc, N = input().split()
    arr = list(input().split())
    # print(arr)
    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    idx = []
    for i in range(len(arr)):
        idx.append(number.index(arr[i]))

    idx = sorted(idx)

    result = []
    for j in range(len(idx)):
        result.append(number[idx[j]])
    result = ' '.join(result)
    print(f'#{test_case} {result}')