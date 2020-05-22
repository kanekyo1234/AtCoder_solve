from collections import deque

# 01BFSの練習


h,w = map(int,input().split())
c = [list(input()) for i in range(h)]

c[h-1][w-1]='g'
d = deque()
g = []
if c[h-1][w-1]=='#':
    asd=1
else:
    asd=0
# 破壊回数。-1未到達
ans = [[-1 for i in range(w)] for j in range(h)]
d.append([0,0])
ans[0][0]=0
g=[h-1,w-1]
# 移動方向
move = [[1,0],[0,1]]

while d:
    p,q = d.popleft()
    for y,x in move:
        if 0<=p+y<h and 0<=q+x<w:
            if ans[p+y][q+x]==-1:
                if c[p+y][q+x]=='.' or c[p+y][q+x]=='g':
                    ans[p+y][q+x]=ans[p][q]
                    d.appendleft([p+y,q+x])
                elif c[p+y][q+x]=='#':
                    ans[p+y][q+x]=ans[p][q]+1
                    d.append([p+y,q+x])

print(ans[g[0]][g[1]]+asd)
