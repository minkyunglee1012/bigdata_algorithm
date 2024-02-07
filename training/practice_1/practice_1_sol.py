# 출처: https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AYYPdof62mIDFARc
import sys
sys.stdin = open("practice_1.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    cards = [int(x) for x in input()]

    # N개의 숫자카드가 주어진다.
    # 숫자가 무조건 0 ~ 9 까지밖에 없다.
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0] * 10
    # 1. 각 숫자가 몇 개 나왔는 지 저장할 리스트 선언
    # 2. 숫자카드를 돌면서, 리스트에 숫자의 개수를 추가해 줌
    # 3. 개수를 저장한 리스트를 돌면서, 가장 맣이 나온 숫자를 반환
    # ( 가장 많이 나온 개수가 동일한 경우에는 더 큰 수를 반환한다. )

    # 0~9 까지 나온 횟수를 저장할 변수 선언
    counting_list = [0] * 10

    # 주어진 숫자카드를 돌면서, 나눈 횟수를 저장함
    for card in cards:
        counting_list[card] += 1

    max_num = 0
    most_num = 0
    # 나온 횟수를 저장한 변수를 순회하면서, 가장 많이 나온 카드를 찾자
    # idx = 숫자카드, counting = 숫자카드가 나온 횟수
    for idx, counting in enumerate(counting_list):
        if counting >= most_num:
            max_num = idx
            most_num = counting

    # print(max_num, most_num)
    print(f'#{test_case} {max_num} {most_num}')
