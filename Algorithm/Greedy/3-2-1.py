# 큰 수의 법칙 두번째

n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 수 구하기
count = (m // (k + 1)) * k
count += m % (k + 1)

result = 0

result = count * first
result += (m - count) * second

print(result)
