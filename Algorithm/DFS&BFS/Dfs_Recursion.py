vertex_list = [1, 2, 3, 4, 5, 6, 7, 8]

edge_list = [(1, 2), (1, 3), (1, 8), (2, 1), (2, 7), (3, 1), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (6, 7), (7, 2), (7, 6), (7, 8), (8, 1), (8, 7)]

ad_list = [[] for i in range(len(vertex_list) + 1)]

for edge in edge_list:
  ad_list[edge[0]].append(edge[1])

visited = [False] * (len(vertex_list) + 1)

def DFS_Recursion(graph, v, vistied):
  # 현 노드 방문 처리
  visited[v] = True
  print(v, end=' ')
  
  # 현재 노드와 연결된 노드 재귀적 방문
  for i in graph[v]:
    if not visited[i]:
      DFS_Recursion(graph, i, visited)


DFS_Recursion(ad_list, 1, visited)
