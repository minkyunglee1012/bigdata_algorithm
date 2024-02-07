# 출처: https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AYYPdof62mIDFARc
import sys
sys.stdin = open("practice_1.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    cards = [int(x) for x in input()]
    # print(cards)
    set_cards_list = list(set(cards))
    # print(list(set(cards)))

    check_dict = {}
    for i in range(len(set_cards_list)):
        check_dict[set_cards_list[i]] = 0

    for j in range(len(cards)):
        if cards[j] in check_dict:
            check_dict[cards[j]] += 1
    # print(check_dict)

    val_list = []
    key_list = []
    for key, val in check_dict.items():
        val_list.append(val)
        key_list.append(key)

    if len(list(set(val_list))) == 1:
        res = max(key_list)
        count = 1
    else:
        ans = val_list.index(max(val_list))
        res = key_list[ans]
        count = max(val_list)

    # print(res, count)




    print(f"#{test_case} {res} {count}")

    # for문 안 쪽에 코드를 작성해주세요

