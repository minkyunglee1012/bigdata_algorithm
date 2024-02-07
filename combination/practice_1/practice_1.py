# 출처: https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
import sys
sys.stdin = open("practice_1.txt", "r")

# 읽은 파일의 한 줄을 읽는다.
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    s = [list(map(int, input().split())) for _ in range(N)]
    import itertools
    result = 0
    # s의 길이만큼 식재료 인덱스 리스트 만들기
    s_index = []
    for i in range(len(s)):
        s_index.append(i)
    # print(s_index)

    # s_index 리스트의 조합을 구하자 (N//2 개씩 요리하므로)
    s_comb = list(itertools.combinations(s_index, N//2))
    # print(s_comb)

    # for문을 사용하여 더해야 할 모든 인덱스들 조합으로 표현
    s_list = []
    for i in range(len(s_comb)):
        s_list.append(list(itertools.permutations(s_comb[i], 2)))
    # print(s_list)

    # 음식을 만들었을 때 시너지 합 구하기
    sum_list = []
    for i in range(len(s_list)):
        s_sum = 0
        for j in range(len(s_list[i])):
            s_sum += s[s_list[i][j][0]][s_list[i][j][1]]
        sum_list.append(s_sum)
    # print(sum_list)

    # 시너지 합 리스트에서 각 양쪽 끝을 뺀 값들 중 최소값 구하기
    s_sub = []
    for i in range(len(sum_list)//2 + 1):
        s_sub.append(abs(sum_list[i] - sum_list[len(sum_list)-1-i]))
    result = min(s_sub)
    print(f"#{test_case} {result}")



