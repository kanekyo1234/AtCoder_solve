"""
from collections import deque
q = deque()
sx,sy=0,0
n,ex,ey=map(int,input().split())
zyama = [list(map(int,input().split())) for _ in range(n)]

h=ex+1
w=ex+1
q.append([sx,sy,0])
global finished 
finished = set()
c=[]
cc=""
for i in range(h):
    cc+="."
for i in range(w):
    c.append(list(cc))
for i in range(n):
    c[ zyama[i][0] ][ zyama[i][1] ]="#"

for i in range(w):
    print(c[i])

def check(x,y):
    if 0<=x and x<h:
        if 0<=y and y<w:
            return True
    return False
count=0
def search():
    while (q):
        x,y,count=q.popleft()
        if check(x,y)==False or (x,y) in finished or c[x][y]=='#':
            continue

        else:
            q.append([x,y-1,count+1])
            q.append([x,y+1,count+1])
            q.append([x+1,y,count+1])
            q.append([x-1,y,count+1])
            q.append([x-1,y+1,count+1])
            q.append([x+1,y+1,count+1])
            finished.add((x,y))
            c[x][y]=count
            if x==ex and y==ey:
                return c[x][y]
print(search())
"""

from collections import deque
q = deque()
sx,sy=201,201
n,ex,ey=map(int,input().split())
ex+=201
ey+=201
zyama = [list(map(int,input().split())) for _ in range(n)]

h=900
w=900
q.append([sx,sy,0])
global finished 
finished = set()
c=[]
cc=""
for i in range(h):
    cc+="."
for i in range(w):
    c.append(list(cc))
for i in range(n):
    c[ zyama[i][0]+201 ][ zyama[i][1]+201 ]="#"

#for i in range(w):
   # print(c[i])

def check(x,y):
    if 0<=x and x<h:
        if 0<=y and y<w:
            return True
    return False
count=0
def search():
    while (q):
        x,y,count=q.popleft()
        if check(x,y)==False or (x,y) in finished or c[x][y]=='#':
            continue

        else:
            q.append([x,y-1,count+1])
            q.append([x,y+1,count+1])
            q.append([x+1,y,count+1])
            q.append([x-1,y,count+1])
            q.append([x-1,y+1,count+1])
            q.append([x+1,y+1,count+1])
            finished.add((x,y))
            c[x][y]=count
            if x==ex and y==ey:
                return c[x][y]
    return -1
print(search())