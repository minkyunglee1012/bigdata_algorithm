### **문제**  
정수로 이루어진 배열 `nums` 과 정수 `target`이 주어진다.  
`nums`에서 2개의 정수의 합이 `target`이 되는 2개 정수의 인덱스를 리스트 형태로 반환하라.  
2개의 합이 `target`이 되는 경우는 반드시 하나이며, 같은 요소를 2번 사용해서 합을 구할 수는 없다.  
리스트 형태로 반환할 때, 순서는 상관없다.
### **제한사항**
- 2 <= nums.length <= 10<sup>4</sup>
- 10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
- 10<sup>9</sup> <= target <= 10<sup>9</sup>
### **예시**  
***Example 1***:

**Input**: *nums = [2, 7, 11, 15], target = 9*  
**Output**: *[0, 1]*
###### 설명: nums[0] + nums[1] == 9, 리턴값 [0, 1]
###
***Example 2***:

**Input**: *nums = [3, 2, 4], taget = 6*  
**Output**: *[1, 2]*

***Example 3***:

**Input**: *nums = [3, 3], taget = 6*  
**Output**: *[0, 1]*
<br/><br/><br/>
출처: 릿코드 [https://leetcode.com/problems/two-sum/description/]

