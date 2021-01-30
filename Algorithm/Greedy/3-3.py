# 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. N은 행의 개수, M은 열의 개수
# 먼저 뽑고자 하는 카드의 행 선택
# 그 다음 선택된 행에 포함된 카드 중 가장 낮은 카드 뽑음
# 처음 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략 세움
# 카드에 적힌 숫자는 1 이상 10,000 이하의 자연수
# 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어짐(1 <= N, M <= 100)

n, m = list(map(int, input().split()))

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)
