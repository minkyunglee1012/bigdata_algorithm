### **문제**  
`words` 리스트와 `pref` 문자열이 주어진다.  
`words` 리스트의 문자열 중에 `pref`가 시작문자열인 문자열의 개수를 리턴해라.  
시작문자열이란 문자열(`s`)의 맨 앞부분부터 시작하는 문자열(`s`)의 부분문자열이다.  
### **제한사항**
- `1 <= words.length <= 100`
- `1 <= words[i].length, pref.length <= 100`
- `words[i]`와 `pref`는 소문자로 이루어져 있다.
### **예시**  
<hr/>

***Example 1***:

**Input**: *words = ["pay","attention","practice","attend"], pref = "at"*  
**Output**: *2*
###### 설명: 
###### 2개의 단어는 "at"로 시작한다. ("attention", "attend")
<hr/>

***Example 2***:

**Input**: *words = ["leetcode","win","loops","success"], pref = "code"*  
**Output**: *0*
###### 설명:
###### 어떠한 단어도 "code"로 시작하지 않는다.
<hr/> 

출처: 릿코드 [https://leetcode.com/problems/counting-words-with-a-given-prefix/description/]