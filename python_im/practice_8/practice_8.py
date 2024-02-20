# testcase 1
# nums, n = [ 2, 5, 1, 3, 4, 7], 3  # [2, 3, 5, 4, 1, 7]

# testcase 2
# nums, n = [1,2,3,4,4,3,2,1], 4  # [1,4,2,3,3,2,4,1]

# testcase 3
nums, n = [1,1,2,2], 2  # [1,2,1,2]

# 아래에 코드를 작성해주세요.


def solution(nums, n):
    nums_x = nums[:n]
    nums_y = nums[n:]
    result = []
    for i in range(len(nums_x)):
        result.append(nums_x[i])
        result.append(nums_y[i])
    return result

print(solution(nums, n))