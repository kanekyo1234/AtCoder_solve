n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n):
    a, b = ab[i]
    ans += (a+b)*((b-a+1)//2)
    if (b-a+1) % 2 == 1:
        ans += (b+a)//2
print(ans)
