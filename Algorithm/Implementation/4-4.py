# 캐릭터가 있는 장소는 1 x 1 크기의 정사각형으로 이뤄진 N x M 크기의 직사각형.
# 각각의 칸은 육지 또는 바다. 육지는 0 바다는 1
# 캐릭터는 동서남북 중 한 곳을 바라본다. 0 : 북 1 : 동 2 : 남 3 : 서
# 맵의 각 칸은 (A, B)로 나타내며 A는 북쪽으로 떨어진 개수, B는 서쪽으로 떨어진 칸의 개수.
# 캐릭터는 상하좌우 움직일 수 있고 바다로 되어있는 곳 갈 수 X

# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 캄이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단 이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

# 알고리즘 문제를 풀 때 지문을 더 자세히 보도록 하고 정말 필요한 변수가 무엇이 있을지 고려해야 할 상황은 무엇이 있는지 분석 한 뒤에 예외를 줄여 코드로 작성해보자

n, m = map(int, input().split())

a, b, d = map(int, input().split())

"""
game_map = [0 for _ in range(m)]

for i in range(m):
  game_map[i] = list(map(int, input().split()))
"""

# 게임 맵 입력 받기
game_map = [list(map(int, input().split())) for _ in range(n)]

# 방문한 육지 체크
visited_stop = [[0] * m for _ in range(n)]
visited_stop[a][b] = 1

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 왼쪽 방향 보기
def turn_left():
  global d
  if d == 0:
    d = 3
  else:
    d -= 1

# 시뮬레이션 시작

# 현재 방문한 곳
count = 1
# 회전 수
turn_count = 0

while True:
  # 왼쪽 보기
  turn_left()
  na = a + dx[d]
  nb = b + dy[d]

  # 육지이고 간적 없는 땅이면 전진
  if game_map[na][nb] == 0 and visited_spot[na][nb] == 0:
    count += 1
    turn_count = 0
    a = na
    b = nb
    visited_spot[a][b] = 1
    continue
  # 가 본적이 없거나 바다인 경우
  else:
    turn_count += 1

  # 네 방향 모두 갈 수 없으면
  if turn_count == 4:
    na = a - dx[d]
    nb = b - dx[d]
    # 뒤로 갈 수 있다면
    if game_map[na][nb] == 0:
      a = na
      b = nb
    # 이 때 뒤가 바다라면
    else:
      break
    # 뒤로 이동 되었으니 다시 회전수 0  
    turn_count = 0

print(count)
