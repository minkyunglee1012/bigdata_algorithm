### **문제**  
정수 리스트 `player1` 과 `player2`가 주어진다. 이 리스트는 각각 플레이어가 볼링에서  쓰러뜨린 핀의 개수를 나타낸다.  
볼링은 `n` 라운드로 되어 있으며, 각 라운드는 `10`개의 핀이 존재한다.  
플레이어가 `i` 라운드에 x<sub>i</sub> 개의 핀을 쳤다고 가졍하면, 플레이어는 아래와 같은 방식으로 점수를 얻는다.  
- 플레이어가 한 라운드에 `10`개의 핀을 친 기록이 2 라운드 이내로 있다면 , 2 * x<sub>i</sub>의 점수를 얻는다.  
- 위 경우 외에는 x<sub>i</sub>의 점수를 얻는다.

플레이어의 총 점수는 `n` 라운드가 지난 후의 점수 총 합이다. 다음 조건에 따라 결과값을 반환하라.  
- player1의 스코어가 player2보다 높으면 `1`을 반환하라.  
- player2의 스코어가 player1보다 높으면 `2`를 반환하라.  
- 무승부일 경우에는 `0`을 반환하라.
### **제한사항**
- n == player1.length == player2.length
- 1 <= n <= 1000
- 0 <= player1[i], player2[i] <= 10
### **예시**  
<hr/>

***Example 1***:

**Input**: *player1 = [4,10,7,9], player2 = [6,5,2,3]*  
**Output**: *1*
###### 설명:
###### player1 총 점수는 4 + 10 + 2 * 7 + 2 * 9  = 46
###### player2 총 점수는 6 + 5 + 2 + 3 = 16
###### player1의 점수가 player2보다 높으므로 1을 반환한다.
<hr/>

***Example 2***:

**Input**: *player1 = [3,5,7,6], player2 = [8,10,10,2]*  
**Output**: *2*  
###### 설명:
###### player1 총 점수, 3 + 5 + 7 + 6 = 21
###### player2 총 점수, 8 + 10 + 2 * 10 + 2 * 2 = 42
<hr/> 

***Example 3***:

**Input**: *player1 = [2,3], player2 = [4,1]*  
**Output**: *0*  
###### 설명:
###### player1 총 점수, 2 + 3 = 5 
###### player2 총 점수, 4 + 1 = 5
<hr/> 
``
출처: 릿코드 [https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/description/]
