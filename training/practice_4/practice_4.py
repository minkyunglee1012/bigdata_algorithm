# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq

import sys
sys.stdin = open("practice_4.txt", "r")

N = int(input())
# print(N)

# 숫자들을 문자화 시켜서 리스트에 담자
num_list = []
for i in range(1, N+1):
    num_list.append(str(i))


# print(num_list)


for i in range(len(num_list)):
    # num_list 순회 하면서, 3, 6, 9 가 들어있을 때 마다 count 해주자
    count = 0
    for j in range(len(num_list[i])):
        if num_list[i][j] == '3' or num_list[i][j] == '6' or num_list[i][j] == '9':
            count += 1

    # count 만큼 '-' 더하자 0이면 숫자 출력, 아니면 '-' * count 출력
    if count ==0:
        pass
    else:
        num_list[i] = '-' * count

print(' '.join(num_list))


# print(num_list)
# print(type(num_list[15][0]))



# print(num_str)

# num_str = num_str.replace('3', '-')
# num_str = num_str.replace('6', '-')
# num_str = num_str.replace('9', '-')






# 아래에 코드를 작성해주세요.



