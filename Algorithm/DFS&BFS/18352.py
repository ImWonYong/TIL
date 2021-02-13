# 백준 18352
from collections import deque


# N = 도시(노드)의 개수, M = 도로(간선)의 개수, K = 거리 정보, X = 출발 도시 번호
n, m, k, x = map(int, input().split())

# N 개의 노드 리스트
vertex_list = [i for i in n]

# m 개의 간선 리스트
edge_list = []
for i in range(m + 1):
  edge_list.append(tuple(map(int, input().split())))

# 인접 리스트 만들기
graph = [[] for i in len(vertex_list) + 1]
for edge in edge_list:
  graph[edge[0]].append(edge[1])


def bfs(start, distance):
  queue = deque()
  queue.append(start)





bfs(k, x)

print(graph)
