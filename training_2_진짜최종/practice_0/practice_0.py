# 출처: https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AYZOEkza5qMDFARc
# 위 사이트에 들어간 후, 문제 풀기를 눌러 작성한 코드(for loop 아래 영역)을 붙여넣고 테스트하세요.
# practice_0.txt에서 맨 위의 숫자를 1로 변경하면 테스트하기 쉽습니다.

import sys
sys.stdin = open("practice_0.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    box_list = list(map(int, input().split()))
    # 작은 숫자대로 소팅한 리스트
    sort_box = sorted(box_list)
    # print(sort_box)

    # 같은 숫자가 들어있으면 그 인덱스를 반환하는 리스트 만들자
    # 그중 가장 큰 숫자가 들어있는 첫 번째 인덱스가 찾고자 하는 답
    get_index = []
    if len(list(set(sort_box))) == 1:
        res = 0
    else:
        for i in range(len(sort_box)-1):
            if sort_box[i+1] - sort_box[i] == 0:
                get_index.append(i)

        res = sort_box.index(sort_box[max(get_index)])

    # print(get_index)
    print(f"#{test_case} {res}")

