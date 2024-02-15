### **문제**  

정렬된 리스트가 주어질 때, 주어진 Type에 따라 주어진 M의 index를 반환하세요.
- 정렬된 리스트는 중복된 값을 갖는다. 
- Type은 LEFT, RIGHT 둘 중 하나의 값을 갖는다.
- Type이 LEFT일 경우에 리스트 안의 중복된 값을 탐색한다면 중복된 값들의 가장 왼쪽 값의 인덱스를 반환한다.
- Type이 RIGHT일 경우에 마찬가지로 중복된 값의 가장 오른쪽 값의 인덱스를 반환한다.

### **예시**  

**Input 1 / Output 1**:  
type, M, arr_1 = "RIGHT", 3, [1, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10]
<br/>
result = 5
<hr/>

**Input 2 / Output 2**:  
type, M, arr_1 = "RIGHT", 7, [1, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10]
<br/>
result = -1
<hr/>

**Input 3 / Output 3**:  
type, M, arr_1 = "LEFT", 3, [1, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10]
<br/>
result = 3
<hr/>

