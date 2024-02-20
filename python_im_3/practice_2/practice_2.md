### **문제**  
배열 `nums`은 [x<sub>1</sub>, x<sub>2</sub>, …, x<sub>n</sub>, y<sub>1</sub>, y<sub>2</sub>, … , y<sub>n</sub> ] 형태와 `2*n` 개의 요소로 이루어져 있다.  
위 배열을 [x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, y<sub>2</sub>, … , x<sub>n</sub>, y<sub>n</sub> ] 의 형태로 반환하세요.  
### **제한사항**
- 1 <= n <= 500
- nums.length == 2n
- 1 <= nums[i] <= 10<sup>3</sup>
### **예시**  
<hr/>

***Example 1***:

**Input**: *nums = [2, 5, 1, 3, 4, 7], n = 3*  
**Output**: *[2, 3, 5, 4, 1, 7]*
###### 설명: 
###### x<sub>1</sub>=2, x<sub>2</sub>=5, x<sub>3</sub>=1, y<sub>1</sub>=3, y<sub>2</sub>=4, y<sub>3</sub>=7 이므로 정답은 [2, 3, 5, 4, 1, 7]
<hr/>

***Example 2***:

**Input**: *nums = [1,2,3,4,4,3,2,1], n = 4*  
**Output**: *[1,4,2,3,3,2,4,1]*
<hr/> 

***Example 3***:

**Input**: *nums = [1,1,2,2], n = 2*  
**Output**: *[1,2,1,2]*
<hr/> 
출처: 릿코드 [https://leetcode.com/problems/shuffle-the-array/description/]