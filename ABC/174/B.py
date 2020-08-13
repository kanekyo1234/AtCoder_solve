n, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    count = (xy[i][0]**2+xy[i][1]**2)**0.5
    if count <= d:
        ans += 1

print(ans)
