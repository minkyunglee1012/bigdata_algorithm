# testcase 1
nums, n = [1,2,3,4,4,3,2,1], 4  # [1,4,2,3,3,2,4,1]

# testcase 2
# nums, n = [1,1,2,2], 2  # [1, 2, 1, 2]

# 아래에 코드를 작성해주세요.

cross_num = []
x_nums = nums[:n]
y_nums = nums[n:]

for i in range(len(x_nums)):
    cross_num.append(x_nums[i])
    cross_num.append(y_nums[i])

print(cross_num)
