n, k = map(int, input().split())

result = 0

while True:
  # n을 k로 나눌 수 있는 가장 가까운 값을 구함
  target = (n // k) * k
  # target를 n에서 빼서 1을 뺴줘야 하는 횟수를 구함
  result += (n - target)
  n = target
  
  # 더 이상 나눌 수 없을 때 반복문 나가기
  if (n < k):
    break
  
  # k로 나눔
  n = n // k
  result += 1

result += (n - 1)

print(result)
  
