# 일곱 난쟁이
import sys
n = 9
l = [int(input()) for _ in range(n)]
l.sort()
total = sum(l)

for i in range(0, n):
  for j in range(i + 1, n):
    if total - l[i] - l[j] == 100:
      for k in range(0, n):
        if i == k or j == k:
          continue
        print(l[k])
      sys.exit(0)
