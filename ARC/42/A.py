n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]
b = [-1]*n
# print()
for i in range(m):
    b[a[i]-1] = i
# print(b)
c = []
for i in range(n):
    c.append([b[i], i+1])
# print(c)
d = sorted(c, key=lambda x: (-x[0], x[1]))
# print(c)

for i in d:
    print(i[1])
