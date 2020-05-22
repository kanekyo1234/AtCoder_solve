from collections import deque
q = deque()
h,w=map(int,input().split())
q.append([0,0,0])
global finished 
finished = set()
c=[]
for i in range(h):
    c.append(list(map(str,input())))


def check(x,y):
    if 0<=x and x<h:
        if 0<=y and y<w:
            return True
    return False

count=0
def search():
    while (q):
        x,y,count=q.popleft()
        print(x,y,count)
        if check(x,y)==False or (x,y) in finished or count==3 :
            
            continue
        else:
            if c[x][y]=='g' :
                print("YES")
                exit()
            elif c[x][y]=='#':
                q.append([x,y-1,count+1])
                q.append([x,y+1,count+1])
                q.append([x+1,y,count+1])
                q.append([x-1,y,count+1])
                finished.add((x,y))
            else:
                q.append([x,y-1,count])
                q.append([x,y+1,count])
                q.append([x+1,y,count])
                q.append([x-1,y,count])
                finished.add((x,y))
            

            
search()
print("NO")