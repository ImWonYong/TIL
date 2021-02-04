# DFS/BFS
대표적인 탐색 알고리즘

## 꼭 필요한 자료구조 기초
- 탐색 : 많은 양의 데이터 중 원하는 데이터 찾느 과정
- 자료구조 : 데이터를 표현하고 관리하고 처리하기 위한 구조
- 삽입, 삭제, 오버플로, 언더플로를 고려하자

### 스택
- 박스 쌓기
- 선입후출(First In Last Out) 또는 후입선출(Last In First Out) 구조
```python
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1] # 최상단 원소부터 출력
```
파이썬에서 스택으 이용하 때에는 별도의 라이브러리 사용할 필요 없다

### 큐
- 대기 줄
- '공정한' 자료구조
- 선입선출(First In First Out) 구조
```python
from collections import deque

# 큐(Queue) 구현을 위해 duque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
print.reverse() # 다음 출력으 윟 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
```
파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조 활용.
deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터 넣고 빼는 속도가 리스트 자료형에 비해 효율적이고 queue 라이브러리를 이용하는 것보다 더 간단.
