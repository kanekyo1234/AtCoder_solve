from collections import deque
q = deque()
h,w=map(int,input().split())
global finished 
finished = set()
c=[]
for i in range(h):
    c.append(list(map(str,input())))
q.append([0,0,0])
if c[h-1][w-1]=='#':
    asd=1
else:
    asd=0
c[h-1][w-1]='s'

def check(x,y):
    if 0<=x and x<h:
        if 0<=y and y<w:
            return True
    return False
global ans
ans=1000

def search():
    while (q):
        x,y,count=q.popleft()
        #print("s")
        global ans
        
        if check(x,y)==False :
            continue

        else:
            if c[x][y]=='#':
                q.append([x,y+1,count+1])
                q.append([x+1,y,count+1])
            else:
                q.appendleft([x,y+1,count])
                q.appendleft([x+1,y,count])
            finished.add((x,y))
            if c[x][y]=="s":
                return count
print(search()+asd)