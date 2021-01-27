# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복함
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

n, k = list(map(int, input().split()))

count = 0

"""
내 풀이

while n >= k && n != 1:
  if(n % k == 0):
    n = n // k
  else:
    n -= 1
  
  count += 1

"""

while n >= k:
  while n % k != 0:
    n -= 1
  n = n // k
  count += 1

while n > 1:
  n -= 1
  count += 1

print(count)
