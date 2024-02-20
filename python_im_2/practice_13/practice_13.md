### **문제**  
`n`개의 요소를 가진 정수형 배열 `nums`과 정수 k 가 주어진다.  
`k`와 길이가 같은 부분집합을 찾고, 부분집합의 합의 평균이 가장 큰 값을 리턴해라.  
어떤 정답도 10<sup>-5</sup> 보다 작을 수는 없다.
### **제한사항**
- n == nums.length
- 1 <= k <= n <= 10<sup>5</sup>
- 10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
### **예시**  
<hr/>

***Example 1***:

**Input**: *nums = [1,12,-5,-6,50,3], k = 4*  
**Output**: *12.75000*
###### 설명: 
###### 최대값 평균은 (12 - 5 - 6 + 50 ) / 4 = 51 / 4 = 12.75
<hr/>

***Example 2***:

**Input**: *nums = [5], k = 1*  
**Output**: *5.00000*
<hr/>
<br/><br/><br/>
출처: 릿코드 [https://leetcode.com/problems/maximum-average-subarray-i/description/]
