from collections import deque
 
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
if grid[H-1][W-1]=='#':
    asd=1
else:
    asd=0
grid[H-1][W-1]='g'
INF = 500**2
sy=sx=gy=gx=0
sy, sx = 0,0
gy, gx = H-1,W-1
current = deque([])
current.append((sy, sx))
dp = [[INF] * (W) for _ in range(H)]
dy = [1,0,]
dx = [0,1,]
dp[sy][sx] = 0
while len(current) > 0:
  cy, cx = current.popleft()
  if cy == gy and cx == gx:
    break
  for i in range(2):
    ny, nx = cy+dy[i], cx+dx[i]
    if 0 <= ny <= H-1 and 0 <= nx <= W-1 and dp[ny][nx] == INF:
      if grid[ny][nx] == '#':
        dp[ny][nx] = dp[cy][cx] + 1
        current.append((ny, nx))
      else:
        dp[ny][nx] = dp[cy][cx]
        current.appendleft((ny, nx))
print(dp[gy][gx]