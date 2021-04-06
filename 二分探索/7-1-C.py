
"""
#!/usr/bin/env python3

import queue

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sx -= 1; sy -= 1; gx -= 1; gy -= 1;

maze = [ list(input()) for _ in range(r) ]

dx = [ -1, 0, 0, 1 ]
dy = [ 0, -1, 1, 0 ]

def bfs(x, y):
    dist = [ [-1]*c for _ in range(r) ]

    que = queue.Queue()
    que.put( [x,y] )
    dist[y][x] = 0

    while not que.empty():
        cur = que.get()
        x, y = cur[0], cur[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= c or ny < 0 or ny >= r:
                continue
            if maze[ny][nx] == '#':
                continue
            if dist[ny][nx] != -1:
                continue
            dist[ny][nx] = dist[y][x] + 1 
            que.put( [nx, ny] )
    
    print(dist[gy][gx])

bfs(sx, sy)

"""