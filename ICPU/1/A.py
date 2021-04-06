n = int(input())
a = list(map(int, input().split()))
aa = sum(a)/n
ans = 0
for i in range(n):
    if aa >= a[i]:
        ans += 1
print(ans)
