n, m, t, p = map(int, input().split())
paper = [[1]*n]*m
print(paper)
dc = [list(map(int, input().split())) for _ in range(t)]
xy = [list(map(int, input().split())) for _ in range(p)]
ans = 0
for i in range(t):
    d, c = dc[i]
    if d == 1:  # 横に折る
        if c <= n-c:
            for j in range(m):
                for h in range(c, c+c):  # 1,2,+1
                    paper[j][h] += paper[j][c-h]
        else:
            for j in range(m):
                for h in range(c-1, n-c-1, -1):  # 2,3 1,4
                    paper[j][h] += paper[j][c+(n-h)]
    else:  # 縦
        if c <= m-c:
            for j in range(c, c+c):
                for h in range(n):  # 1,2,+1
                    paper[c][h] += paper[c-j][h]
        else:
            for j in range(c-1, m-c-1, -1):
                for h in range(n):  # 2,3 1,4
                    paper[j][h] += paper[c+(m-j)][h]
print(paper)


for i in range(p):
    x,y=xy[i]
    ans+=paper[i][j]
print(ans)