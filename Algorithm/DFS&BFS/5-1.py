# n, m 입력
n, m = map(int, input().split())

# graph 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):
  # 그래프 가로 제로 범위를 벗어나면 안됨
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False

  # 현 좌표가 얼음이고 방문한 적 없다면 방문 처리 해야 함
  if graph[x][y] == 0:
    graph[x][y] = 1

    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)

    return True

  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)
