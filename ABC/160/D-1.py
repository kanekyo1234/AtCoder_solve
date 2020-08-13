n, x, y = map(int, input().split())
ans = [0]*n
x -= 1
y -= 1
for i in range(n-1):
    for j in range(i+1, n):
        # print("DFGH")
        ans[min(j-i, abs(x-i)+abs(y-j)+1)] += 1

for i in range(1, n):
    print(ans[i])
