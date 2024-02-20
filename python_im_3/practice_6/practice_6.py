# testcase 1
nums, k = [3, 1, 2, 2, 2 ,1, 3], 2  # 4

# testcase 2
# nums, k = [1, 2, 3, 4], 1  # 0

# 아래에 코드를 작성해주세요.

count = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j] and (i * j) % k == 0:
            count += 1

print(count)