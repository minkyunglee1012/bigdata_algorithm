# testcase 1
nums = [1, 2, 2, 3]  # True

# testcase 2
# nums = [6, 5, 4, 4]  # True

# testcase 3
# nums = [1, 3, 2]  # False

# 아래에 코드를 작성해주세요.


def isMonotonic(nums):
    increasing = decreasing = True

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            increasing = False
        if nums[i] < nums[i + 1]:
            decreasing = False

    return increasing or decreasing

print(isMonotonic((nums)))