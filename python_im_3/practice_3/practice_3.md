### **문제**  
문자열 리스트 `names` 와 서로 다른 양의 정수 `heights` 리스트 가 주어지고, 두 배열의 길이는 `n`이다  
각각의 인덱스가 `i`일 때, `names[i]`와`heights[i]`는  `i`번째 사람의 이름과 키를 나타낸다.  
사람의 키 순서로 내림차순해서 `이름 리스트`를 리턴하세요.  
### **제한사항**
- n == names.length == heights.length
- 1 <= n <= 10<sup>3</sup>
- 1 <= names[i].length <= 20
- 1 <= heights[i] <= 10<sup>5</sup>
- `names[i]`는 영어 소문자와 대문자로 이루어져있다.
- `heights`의 모든 값은 서로 다른 값이다.
### **예시**  
<hr/>

***Example 1***:

**Input**: *names = ["Mary","John","Emma"], heights = [180,165,170]*  
**Output**: *["Mary","Emma","John"]*
###### 설명: 
###### Mary 가 가장 크고, 그 이후로 Emma 와 John이 크다.
<hr/>

***Example 2***:

**Input**: *names = ["Alice","Bob","Bob"], heights = [155,185,150]*  
**Output**: *["Bob","Alice","Bob"]*
<hr/> 
출처: 릿코드 [https://leetcode.com/problems/sort-the-people/description/]