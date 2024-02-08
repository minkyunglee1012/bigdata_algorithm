# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh

import sys
sys.stdin = open("practice_1.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    building_list = list(map(int, input().split()))
    count = 0
    # print(N, building_list)
    for i in range(2, len(building_list)-2):
        # 조망권 획득하기 위해서 양 옆 2개씩 크기 확인하기 위해 변수 할당
        a, b, c, d = building_list[i - 2], building_list[i - 1], building_list[i + 1], building_list[i + 2]
        # 4곳 중 가장 큰 곳과 비교하면 되므로 max 값 구하기
        max_building = max(a, b, c, d)
        # max보다 크면 조망권을 획득하므로 차이 구해서 count 하기
        if building_list[i] > max_building:
            count += building_list[i] - max_building
        # while (building_list[i] > building_list[i-2] and building_list[i] >
        #        building_list[i-1] and building_list[i] > building_list[i+1] and
        #        building_list[i] > building_list[i+2]):
        #     count += 1
        #
        #     building_list[i-2] += 1
        #     building_list[i-1] += 1
        #     building_list[i+1] += 1
        #     building_list[i+2] += 1
        # building_list[i-2], building_list[i-1],  building_list[i+1], building_list[i+2] = a, b, c, d

    print(f"#{test_case} {count}")
    # for문 안 쪽에 코드를 작성해주세요
