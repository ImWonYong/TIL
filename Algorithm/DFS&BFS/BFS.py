from collections import deque

vertex_list = [1, 2, 3, 4, 5, 6, 7, 8]

edge_list = [(1, 2), (1, 3), (1, 8), (2, 1), (2, 7), (3, 1), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (6, 7), (7, 2), (7, 6), (7, 8), (8, 1), (8, 7)]

ad_list = [[] for i in range(len(vertex_list) + 1)]

for edge in edge_list:
  ad_list[edge[0]].append(edge[1])

visited = [False] * (len(vertex_list) + 1)

def BFS(graph, start, visited):
  # 큐를 생성하고 시작
  queue = deque([start])

  # 방문처리
  visited[start] = True
  
  # 큐가 빌 때까지
  while queue:
    # 큐에서 하나 뽑고 출력
    current = queue.popleft()
    print(current, end = ' ')
    # 연결되어 있고, 아직 방문하지 않은 원소 큐에 넣기
    for i in graph[current]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

BFS(ad_list, 1, visited)
