### **문제**  
두 리스트 `nums1`과`nums2`가 주어질 때, 아래 조건에 맞게 사이즈가 `2`인 리스트 `answer`를 반환하세요.  
- `answer[0]`은 `nums1`에 존재하지만, `nums2`에는 존재하지 않는 정수 목록  
- `answer[1]`은 `nums2`에 존재하지만, `nums1`에는 존재하지 않는 정수 목록  
**Note**: 반환되는 정수 리스트의 순서는 상관없다.  
### **제한사항**
- 1 <= nums1.length, nums2.length <= 1000
- 1000 <= nums1[i], nums2[i] <= 1000
### **예시**  
<hr/>

***Example 1***:

**Input**: *nums1 = [1,2,3], nums2 = [2,4,6]*  
**Output**: *[[1,3],[4,6]]*
###### 설명: 
###### nums1에서 nums1[1] = 2 는 nums2의 0 인덱스에 존재한다.
###### nums1[0], nums1[2] 는 nums2에 존재하지 않는다.
###### 그러므로 answer[0] = [1, 3] 
###### nums2에서 nums2[0] = 2 는 nums1의 1 인덱스에 존재한다.
###### nums2[1], nums2[2] 는 nums1에 존재하지 않는다.
###### 그러므로 answer[1] = [4, 6] 
<hr/>

***Example 2***:

**Input**: *nums1 = [1,2,3,3], nums2 = [1,1,2,2]*  
**Output**: *[[3], []]*  
###### 설명: 
###### nums1에서 nums1[2], nums1[3]은 nums2에 존재하지 않는다. 
###### nums1[2] == nums1[3] 때문에, 그들의 값은 오직 하나가 되고 answer[0] = [3]
###### nums2의 모든 정수는 nums1에 존재한다. 그러므로, answer[1] = []
<hr/>
출처: 릿코드 [https://leetcode.com/problems/find-the-difference-of-two-arrays/description/]