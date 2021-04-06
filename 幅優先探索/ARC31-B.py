from collections import deque
import copy
q = deque()
global finished 
finished = set()
c=[]
for i in range(10):
    c.append(list(map(str,input())))

def check(x,y):
    if 0<=x and x<10:
        if 0<=y and y<10:
            return True
    return False
count=0
def search():
    finished = set()#これ更新しないとだめ
    while (q):
        x,y=q.popleft()
        
        if check(x,y)==False or (x,y) in finished or box[x][y]=='x':
            continue
        else:
            q.append([x,y-1])
            q.append([x,y+1])
            q.append([x+1,y])
            q.append([x-1,y])
            finished.add((x,y))
            box[x][y]="e" #通ったらe
            #print(box[x])
            #print()
        
        
    for i in range(10):
        if box[i].count("o")!=0:
            return False
    else:
        return True

for i in range(10):
    for j in range(10):
        #print(i,j)
        box=copy.deepcopy(c)
        box[i][j]="o"
        q.append([i,j])
        if search():
            print("YES")
            exit()
print("NO")


    