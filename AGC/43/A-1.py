from collections import deque
h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
if c[h-1][w-1]=='#':
    asd=1
else:
    asd=0
moves = ((1, 0), (0, 1),)
sy=0
sx=0
ty=h-1
tx=w-1
def bfs(sy, sx):
  dist = [[float('inf')]*w for _ in range(h)]
  dist[sy][sx] = 0 
  q = deque([[sy, sx]])
  while q:
    y, x = q.popleft()
    #print(q)
    for dy, dx in moves:
      ny = y + dy 
      nx = x + dx 
      if 0 <= ny < h and 0 <= nx < w and dist[ny][nx] == float('inf'):
        if c[ny][nx] == '#':
          dist[ny][nx] = dist[y][x] + 1
          q.append([ny, nx])
        else:
          dist[ny][nx] = dist[y][x]
          q.appendleft([ny, nx])
    print(dist)
  return dist 
dist = (bfs(sy, sx))
print( dist[ty][tx]+asd)