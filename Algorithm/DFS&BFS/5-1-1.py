from collections import deque

# n, m 입력
n, m = map(int, input().split())

# graph 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):

    # 칸막이거나 방문했음
    if graph[x][y] == 1:
        return False

    # 얼음이라면
    queue = deque()
    queue.append((x, y))

    graph[x][y] = 1

    while queue:

        x, y = queue.popleft()

        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((nx >= 0 and nx < n) and (ny >= 0 and ny < m)) and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1

    return True


result = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            result += 1

print(result)
