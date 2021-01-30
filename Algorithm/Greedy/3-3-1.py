n, m = list(map(int, input().split()))

result = 0

for i in range(n):
  data = list(map(int, input().split()))

  min_value = 10001
  for j in data:
    min_value = min(min_value, j)
  
  result = max(result, min_value)

print(result)

