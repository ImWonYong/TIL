# 백준 17425
# 약수의 합
# 약수의 합을 구하는 데 배수의 개념을 이용한다.
# 1 - N 까지 모든 수의 약수의 합들의 합을 구하려고 한다면 각 수의 배수를 구해서 배수들이 들어갈 곳에 더해주면 된다.
# 테스트 케이스 방식의 문제풀이 중에서 변하지 않는 값들이 있다면 반복하지 말고 미리 구한 뒤에 재사용하는 것이 좋다.

MAX = 1000000

d = [1] * (MAX + 1)
s = [0] * (MAX + 1)

for i in range(2, MAX + 1):
  j = 1
  while i * j <= MAX:
    d[i * j] += i
    j += 1

for i in range(1, MAX + 1):
  s[i] = s[i - 1] + d[i]

t = int(input())
ans = []

for _ in range(t):
  n = int(input())
  ans.append(s[n])

print('\n'.join(map(str, ans)) + '\n')
