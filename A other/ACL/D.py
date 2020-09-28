n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
a2 = []
for i in range(n-1):
    a2.append(abs(a[i]-a[i+1]))
print(a2)
