# 재귀적인 행동을 할 때는 데이터의 순서 등을 동일하게 유지해 주느 것도 중요하다.
# bcd의 순열을 구하고 앞에 a를 붙이는 방식을 이용하여 순열을 구해봄
def Permutation(str, prefix):
  if str == "":
    print(prefix)
  else:
    for i in range(len(str)):
      rem = str[0:i] + str[i + 1:]
      Permutation(rem, prefix + str[i])

U = "abcd"

Permutation(U, "")
