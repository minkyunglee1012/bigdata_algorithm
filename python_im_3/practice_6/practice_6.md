### **문제**  
길이가 `n`인 리스트 `nums`와 정수 `k`가 주어질 때,  
`nums[i] == nums[j]` 이고 `( i * j )` 가 `k`로 나눠지는 `0 ≤ i < j < n` 범위의 `(i, j)`를 리턴하세요.
### **제한사항**
- 1 <= nums.length <= 100
- 1 <= nums[i], k <= 100
### **예시**  
<hr/>

***Example 1***:

**Input**: *nums = [3, 1, 2, 2, 2 ,1, 3], k = 2*  
**Output**: *4*
###### 설명: 
###### 4개의 쌍이 조건에 만족한다.
###### nums[0] == nums[6], 0 * 6 == 0 이고 2로 나누어 떨어진다.
###### nums[2] == nums[3], 2 * 3 == 6 이고 2로 나누어 떨어진다.
###### nums[2] == nums[4], 2 * 4 == 8 이고 2로 나누어 떨어진다.
###### nums[3] == nums[4], 3 * 4 == 12 이고 2로 나누어 떨어진다.
<hr/>

***Example 2***:

**Input**: *nums = [1, 2, 3, 4], k = 1*  
**Output**: *0*  
<hr/> 

출처: 릿코드 [https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/]
