# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰수를 만들자
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속으로 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징

n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
  for i in range(k):
    if (m == 0):
      break;
    result += first
    m -= 1;
  
  if(m == 0):
    break
  result += second
  m -= 1

print(result)
