def Permutation(str, prefix):
  if str == "":
    print(prefix)
  else:
    for i in range(len(str)):
      rem = str[0:i] + str[i + 1:]
      Permutation(rem, prefix + str[i])

U = "abcd"

Permutation(U, "")
