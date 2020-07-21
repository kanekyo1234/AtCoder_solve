n = int(input())
a = list(map(int, input().split()))

x1 = 0
for i in range(1, n, 2):
    x1 += a[i]*2

x1 = sum(a)-x1
ans = [x1]
for i in range(n-1):
    ans.append((a[i]-ans[i]//2)*2)

print(*ans)
