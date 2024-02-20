### **문제**  

배열 nums은 [x1, x2, …, xn, y1, y2, … , yn ] 형태와 2*n 개의 요소로 이루어져 있다.
위 배열을 [x1, y1, x2, y2, … , xn, yn ] 의 형태로 출력하세요.

### **제한사항** 
- `1 <= n <= 500`
- `nums.length == 2n`
- `1 <= nums[i] <= 10^3`

### **예시**  

**Input 1 / Output 1**:  
nums, n = [ 2, 5, 1, 3, 4, 7 ], 3  
<br/>
result = [2, 3, 5, 4, 1, 7]
<hr/>

**Input 2 / Output 2**:  
nums, n = [1,2,3,4,4,3,2,1], 4  
<br/>
result = [1,4,2,3,3,2,4,1]
<hr/>

**Input 3 / Output 3**:  
nums, n = [1,1,2,2], 2  
<br/>
result = [1,2,1,2]  
<br/><br/><br/>
출처: 릿코드 [https://leetcode.com/problems/shuffle-the-array/description/]
