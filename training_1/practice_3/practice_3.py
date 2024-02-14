# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWZ2IErKCwUDFAUQ
import sys
sys.stdin = open("practice_3.txt", "r")

from itertools import combinations

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    # 조합을 이용해서 숫자를 3개씩 나열하는 리스트 만든 후 각각의 합을 구하는 리스트를 만들자
    perm_list = list(combinations(arr, 3))

    perm_sum = []
    for i in range(len(perm_list)):
        perm_sum.append(sum(perm_list[i]))
    perm_sum = list(set(perm_sum))

    for i in range(4):
        perm_sum.remove(max(perm_sum))

    ans = max(perm_sum)
    print(f"#{test_case} {ans}")
