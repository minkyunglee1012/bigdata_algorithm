# testcase 1
nums, target = [2, 7, 11, 15], 9  # [0, 1]

# testcase 2
# nums, target = [3, 2, 4], 6  # [1, 2]
#
# testcase 3
# nums, target = [3, 3], 6  # [0, 1]

# 아래에 코드를 작성해주세요.


for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
