def costBuyN(a, b, n):
  d = 0
  while n // (10 ** d) >= 1:
    d += 1
  return a * n + b * d

A, B, X = [int(i) for i in input().split()]

l = 0
r = 10 ** 9 + 1

while r-l > 1:
  c = (l + r) // 2
  if X < costBuyN(A, B, c):
    r = c
  else:
    l = c

print(l)
