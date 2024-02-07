# 출처: https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
import sys
sys.stdin = open("practice_1.txt", "r")

# 읽은 파일의 한 줄을 읽는다.
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    s = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 리스트의 n개의 조합을 구하는 함수
    def get_comb(arr, n):
        res = []
        if n == 1:
            return [[i] for i in arr]

        for i in range(len(arr)):
            val = arr[i]
            for rest in get_comb(arr[i+1:], n-1):
                res.append([val] + rest)

        return res

    # 1. 레시피를 대신 할 인덱스 리스트를 만들자 ( N 크기 )
    # 2. 인덱스 리스트를 대상으로 N//2 개의 조합을 구하자.
    # 3. N//2 개의 구한 조합을 순회하면서
    # 4. A가 확정된 조합에 의해 결정되는 B 조합을 구하자
    # 5. 각 조합(레시피)에서 2개의 조합을 구하고, 시너지를 구하자.
    res = 10000000000
    half = N // 2
    # 1번에 해당하는 N 크기의 인덱스 리스트
    # num_list = []
    # for i in range(N):
    #     num_list.append(i)
    num_list = [i for i in range(N)]
    comb_list = get_comb(num_list, half)

    # half개의 조합을 대상으로 전체 순회
    for comb in comb_list:
        # a 레시피 조합이 정해졌다 치고,
        # 전체 목록 중 a에 포함되어 있지 않으면, b에 추가
        a_list = comb  # [0, 1]
        b_list = []

        # 전체 레시피 목록을 돌면서, 해당 레시피가 a에 포함되지 않으면
        # b 레시피에 존재하는 것이므로, b 리스트에 추가
        for num in num_list:
            if num not in a_list:
                b_list.append(num)

        # a 레시피 목록에서 2개씩 조합한 목록을 가져옴
        a_comb_list = get_comb(a_list, 2)
        a_sum = 0 # a 요리 시너지의 합을 저장할 변수
        # 2개씩 조합한 목록을 돌면서
        # 각 조합의 시너지를 구한다.
        for a_comb in a_comb_list: # ex : a_comb => [0, 1]
            i, j = a_comb
            a_sum += s[i][j] + s[j][i]

        b_comb_list = get_comb(b_list, 2)
        b_sum = 0
        for b_comb in b_comb_list:
            i, j = b_comb
            b_sum += s[i][j] + s[j][i]

        # 두 요리의 차의 절대값이 여태까지 나온 모든 시너지보다 작다면
        # 최소 맛의 차이를 갱신함

        res = min(res, abs(a_sum - b_sum))

    print(f"#{test_case} {res}")