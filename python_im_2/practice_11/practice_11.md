### **문제**  
배열 값이 순서가 지날수록 값이 같거나 커지거나, 값이 같거나 작아지는 배열을 단조배열이라고 합니다.  
단조증가배열은 `i <= j`,`nums[i] <= nums[j]` 입니다.  
단조감소배열은 `i <= j`,`nums[i] >= nums[j]` 입니다.  
정수 배열 `nums`가 주어질 때, nums가 단조배열이면 `True`, 아니면 `False` 를 반환하세요.
### **제한사항**
- 1 <= nums.length <= 10<sup>5</sup>
- 10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>
### **예시**  
***Example 1***:

**Input**: *nums = [1, 2, 2, 3]*  
**Output**: *True*

***Example 2***:

**Input**: *nums = [6, 5, 4, 4]*  
**Output**: *True*

***Example 3***:

**Input**: *nums = [1, 3, 2]*  
**Output**: *False*
<br/><br/><br/>
출처: 릿코드 [https://leetcode.com/problems/monotonic-array/description/]
