from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()

  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 미로 범위 벗어나면 안됨
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      # 괴물을 만나면 안됨
      if graph[nx][ny] == 0:
        continue

      # 범위 내일 때
      if graph[nx][ny] == 1:
        if nx == 0 and ny == 0:
          continue
        else:
          graph[nx][ny] = graph[x][y] + 1
          queue.append((nx, ny))

  return graph[n - 1][m - 1]

  

# 1100
# 0110
# 0011
# 0001


print(bfs(0, 0))
print(graph)
