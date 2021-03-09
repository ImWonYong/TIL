# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오
# 입력 예제 3 16
# 출력 예제
# 3
# 5
# 7
# 11
# 13

# 에라토스테네스의 체
MAX = 1000000

checked = [0] * (MAX + 1)
checked[0] = checked[1] = True


for i in range(2, MAX + 1):
  if i * i > MAX:
    break
  if not checked[i]:
    j = i + i
    while j <= MAX:
      checked[j] = True
      j += i


m, n = map(int, input().split())


for i in range(m, n + 1):
  if checked[i] == False:
    print(i)
