# testcase 1
# nums, k = [1,12,-5,-6,50,3], 4  # 12.75000

# testcase 2
nums, k = [5], 1  # 5.00000

# 아래에 코드를 작성해주세요.


def findMaxAverage(nums: list[int], k: int) -> float:
    mean_list = []

    if len(nums) == 1:
        return nums[0]

    for i in range(len(nums) - k +1):
        mean_list.append((sum(nums[i: k + i])) / k)
        max_mean = max(mean_list)
    return max_mean

print(findMaxAverage([0,1,1,3,3], 4))

