# 내 풀이
value = list(input())

row = value[0]
column = int(value[1])

# 이동할 수 있는 8가지 방법
# 이 부분은 참고함
move_types = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

count = 0

for move_type in move_types:
  new_row = chr(ord(row) + move_type[0])
  new_column = column + move_type[1]
  if ord(new_row) < 97 or new_column < 1 or ord(new_row) > 104 or new_column > 8:
    continue
  else:
    print(new_row, new_column)
    count += 1

print(count)

# 책의 풀이

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
step = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1
    
print(result)
