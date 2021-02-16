# 배수의 반대는 약수다.
# 3의 배수라면 3의 약수다.
# 3의 약수라면 3의 배수다.

n = int(input())

result = 0

for i in range(1, n + 1):

  result += (n // i) * i

print(result)
