# 백준 18352
from collections import deque

# N = 도시(노드)의 개수, M = 도로(간선)의 개수, K = 거리 정보, X = 출발 도시 번호
n, m, k, x = map(int, input().split())

# N 개의 노드 리스트
vertex_list = [i for i in range(n)]

# m 개의 간선 리스트
edge_list = []
for i in range(m):
  edge_list.append(tuple(map(int, input().split())))

# 인접 리스트 만들기
graph = [[] for i in range(len(vertex_list) + 1)]
for edge in edge_list:
  graph[edge[0]].append(edge[1])

d_graph = [-1] * (n + 1)

# bfs 해보자
queue = deque()
# 출발 도시 번호 넣기
queue.append(x)
d_graph[x] = 0

while queue:
  current = queue.popleft()

  for i in graph[current]:
    if d_graph[i] == -1:
      queue.append(i)
      d_graph[i] = d_graph[current] + 1

result = []
for i, value in enumerate(d_graph):
  if value == k:
    result.append(i)

if result:
  for i in result:
    print(i)
else:
  print(-1)
