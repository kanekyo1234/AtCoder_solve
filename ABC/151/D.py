
from collections import deque
def check(x,y):
    if 0<=x and x<h:
        if 0<=y and y<w:
            return True
    return False

count=0
def bfs():
    while (q):
        x,y,count=q.popleft()#popleftにしてるおかげで幅優先になる　popだと深さになって最初の入力例が８になる
        
        if check(x,y)==False or (x,y) in finished or c[x][y]=='#':
            continue

        else:
            q.append([x,y-1,count+1])
            q.append([x,y+1,count+1])
            q.append([x+1,y,count+1])
            q.append([x-1,y,count+1])
            finished.add((x,y))
            bfscount.append(count)
    print(bfscount)
    return max(bfscount)

q = deque()
h,w=map(int,input().split())
finished = set()
c=[]
for i in range(h):
    c.append(list(map(str,input())))
ans=[]
bfscount=[]
for i in range(h):
    for j in range(w):
        if c[i][j]==".":
            q.append([i,j,0])
            ans.append(bfs())
            finished = set()
            bfscount=[]
print(max(ans))