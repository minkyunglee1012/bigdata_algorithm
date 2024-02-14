# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXuUo_Tqs9kDFARa

import sys
sys.stdin = open("practice_0.txt", "r")

T = int(input())
result = ""
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A, B, C, D = list(map(int, input().split()))
    # for문 안 쪽에 코드를 작성해주세요
    # 아래 ans는 자유롭게 바꾼 후 정답을 출력하세요.
    ans = min(B, D) - max(A, C)

    if ans < 0:
        ans = 0

    result += f"#{test_case} {ans}\n"
print(result)

