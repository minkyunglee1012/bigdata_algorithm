# testcase 1
# player1, player2 = [4,10,7,9], [6,5,2,3]  # 1

# testcase 2
# player1, player2 = [3,5,7,6], [8,10,10,2]  # 2

# testcase 3
player1, player2 = [2, 3], [4, 1]  # 0

# 아래에 코드를 작성해주세요.

bowl_sum_player1 = 0
bowl_sum_player2 = 0

if player1[0] == 10 or player1[1] == 10:
    for i in range(0, 2):
        bowl_sum_player1 += player1[i]
    for i in range(2, len(player1)):
        bowl_sum_player1 += player1[i] * 2

if player2[0] == 10 or player2[1] ==10:
    for i in range(0,2):
        bowl_sum_player2 += player2[i]
    for i in range(2, len(player2)):
        bowl_sum_player2 += player2[i] * 2

if bowl_sum_player1 > bowl_sum_player2:
    print(1)
elif bowl_sum_player1 < bowl_sum_player2:
    print(2)
else:
    print(0)

