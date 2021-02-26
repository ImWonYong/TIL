m, n = map(int, input().split())

# 유클리드 호제법
def gcd(a, b):
    if b!= 0:
        return gcd(b, a%b)
    else:
        return a
    
g = gcd(m, n)

l = int(m * n / g)

print(g, l)
