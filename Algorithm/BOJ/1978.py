n = int(input())

l = list(map(int, input().split()))

result = 0

for i in l:
  # 1으 소수 아니랍니다
  if (i < 2):
    continue
  else:
    isPrime = True
    for j in range(2, i):
      if j * j <= i:
        if i % j == 0:
          isPrime = False
          break
    if isPrime:
      result += 1

print(result)
