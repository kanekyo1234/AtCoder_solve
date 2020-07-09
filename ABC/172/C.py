n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = a+b
c.sort()
for i in range(1, n+m):
    c[i] += c[i-1]
for i in range(n+m):
    if c[i] > k:
        print(i)
        break
else:
    print(n+m)
