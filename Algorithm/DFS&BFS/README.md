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

### 재귀 함수
- 자기 자신을 다시 호출하는 함수

```python
def recursive_function():
	print(‘재귀 함수를 호출합니다.’)
	recursive_function()

recursive_function()
```
이 코드는 무한히 호출됨.

- 재귀 함수는 종료 조건이 필요함
- 언제 끝날지, 종료 조건을 꼭 명시해야 함.
```python
def recursive_function(i):
	# 100번째 출력했을 때 종료되도록 종료 조건 명시
	if i == 100:
		return
	print(I, ‘번째 재귀 함수에서’, i + 1, ‘번째 재귀 함수를 호출합니다.’)
	recursive_function(i + 1)
	print(i, ‘번째 재귀 함수를 종료합니다.’)

recursive_function(1)
```
- 컴퓨터 내부에서 재귀 함수의 수행은 스택 자려구조를 이용함.
- 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해 간편 구현할 수 있다.
- DFS가 대표적인 예
```python
# 반복적으로 구현한 n!
def factorial_iterative(n):
	result = 1
	# 1부터 n까지의 수를 차례대로 곱하기
	for i in range(1, n + 1):
		result *= i
	return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
	if n <= 1:
		return 1
	return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print(‘반복적으로 구현:’, factorial_iterative(5))
print(‘재귀적으로 구현:’, factorial_recursive(5))
```
재귀 함수를 이용하는 대표적인 예제인 펙토리얼 문제.
반복문 대신에 재귀 함수를 사용했을 때 얻을 수 있는 장점은?
- 반복문보다 더 간결함.(점화식을 그대로 코드로 옮겼기 때문)
- 점화식은 특정한 어떤 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것을 의미

유클리드 호제법
	- 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 할 때, A와 B의 최대공약수는 B와 R의 최대 공약수와 같다.
```python
def gcd(a, b):
	if a % b == 0:
		return b
	else:
		return gcd(b, a % b)

print(gcd(192, 162))
```
## 탐색 알고리즘 DFS/BFS

### DFS(Depth-FIrst Search)
- 깊이 우선 탐색
- 그래프의 깊은 부분을 우선으로 탐색하는 알고리즘

그래프의 기본 구조
- 노드, 간선
- 두 노드가 간선으로 연결되어 있다면 ‘두 노드는 인접하다’라고 표현

프로그래밍에서 그래프를 나타내는 2가지 방식
- 인접 행렬: 2차원 배열로 그래프 연결 관계를 표현하는 방식
- 인접 리스트: 리스트로 그래프의 연결 관계를 표현하는 방식

인접 행렬 방식
- 연결이 되지 않은 노드끼리는 무한의 비용이라고 작성
```python
INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
	[0, 7, 5],
	[7, 0, INF],
	[5, INF, 0]
]

print(graph)
```

인접 리스트 방식
- 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
```python
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3))

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)
```

인접 행렬과 인접 리스트의 차이
- 메모리 측면에서 인접 행렬 방식은 모든 관계 저장하므로 노드 개수가 많을 수록 메모리 낭비됨. 인접 리스트는 연결 정보만 저장하기 때문에 메모리 효율적으로 사용.
- 위와 같은 속성으로 인해 특정 두 노드가 연결되어 있는지에 대한 정보 얻는 속도 인접 리스트가 느림.
- 특정한 노드와 연결된 모든 인접 노드를 순회하는 경우, 인접 리스트 방식이 인접 행렬 방식에 비해 메모리 낭비 적음.

DFS 알고리즘의 구체적인 동작
- 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙하게 들어가서 노드를 방문한 후 다시 돌아가 다른 경로를 탐색하는 알고리즘
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드 꺼냄
3. 더 이상 2번의 과정을 수행할  수 없을 때까지 반복
```python
# DFS 메서드 정의
def dfs(graph, v, visited):
	# 현재 노드를 방문 처리
	visited[v] = True
	print(v, end=‘ ‘(
	# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for I in graph[v]:
		if not visited[I]:
			dfs(graph, I, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

### BFS(Breadth-First Search)
- 너비 우선 탐색
- 가까운 노드부터 우선적으로 탐색하는 알고리즘
1, 탐색 시작 노드를 큐에 삽입하고 방문 처리.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입
3. 2번 과정을 더 이상 수행 할 수 없을 때까지 반복
