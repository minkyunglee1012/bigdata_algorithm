# testcase 1
nums1, nums2 = [1,2,3], [2,4,6]  # [[1,3],[4,6]]

# testcase 2
# nums1, nums2 = [1,2,3,3], [1,1,2,2]  # [[3], []]

# 아래에 코드를 작성해주세요.

answer =[[],[]]
for idx in range(len(nums1)):
    if nums1[idx] not in nums2:
        answer[0].append(nums1[idx])
for idx in range(len(nums2)):
    if nums2[idx] not in nums1:
        answer[1].append(nums2[idx])

print(answer)