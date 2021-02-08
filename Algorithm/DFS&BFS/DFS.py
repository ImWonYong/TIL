# 내가 짜본 DFS

vertex_list = [0, 1, 2, 3, 4, 5, 6]
edge_list = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 4), (2, 5), (3, 1),
             (4, 2), (4, 6), (5, 2), (6, 4)]

adjacency_list = [[] for vertex in vertex_list]

for edge in edge_list:
    adjacency_list[edge[0]].append(edge[1])

visited = []

def DFS(adjacency_list, start, visited):
  # 스택에 시작되는 vertex 넣기
  stack = [start]

  # 빈 Sequence(String / Tuple / List)는 False 값을 가진다.
  while stack:
      현재 스택 맨위의 vertex를 뺴고 방문 처리
      current = stack.pop()
      visited.append(current)
      인접한 vertex를 찾고 방문한 적이 없다면 stack에 넣기
      for adjacency in adjacency_list[current]:
          if not adjacency in visited:
            stack.append(adjacency)

  return visited

print(DFS(adjacency_list, 0, visited))
