# 골드바흐의 추측
MAX = 1000000

checked = [0] * (MAX + 1)

checked[0] = checked[1] = True

primes = []

for i in range(2, MAX):
  if i * i > MAX:
    break
  if not checked[i]:
    primes.append(i)
    j = i + i
    while j <= MAX:
      checked[j] = True
      j += i

primes = primes[1:]
while True:
  value = int(input())
  if value == 0:
    break

  for i in primes:
    if not checked[value - i]:
      print("{0} = {1} + {2}".format(value, i, value - i))
      break
