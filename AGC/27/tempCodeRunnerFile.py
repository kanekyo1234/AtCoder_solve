n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    if a[i] <= x:
        ans += 1
        x -= a[i]
    else:
        break

print(ans)
