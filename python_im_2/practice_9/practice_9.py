# testcase 1
nums = [4,3,2,7,8,2,3,1]  # [5, 6]

# testcase 2
# nums = [1, 1]  # [2]

# 아래에 코드를 작성해주세요.

# len(nums)

result = []
for idx in range(1, len(nums)+1):
    if (idx not in nums):
        result.append(idx)
print(result)