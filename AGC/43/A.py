from collections import deque
q = deque()
h,w=map(int,input().split())
global finished 
finished = set()
c=[]
for i in range(h):
    c.append(list(map(str,input())))
cans=[[300 for _ in range(w)] for _ in range(h)]
#print(cans)
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
        x,y,count=q.pop()
        #print(q)
        global ans
        
        if check(x,y)==False :
            continue

        else:
            if c[x][y]=='#':
                
                if c[max(0,x-1)][y]!='#' or c[x][max(y-1,0)]!='#':
                    if cans[x][y]==300 or count+1<cans[x][y]:
                        cans[x][y]=count+1
                        q.append([x,y+1,count+1])
                        q.append([x+1,y,count+1])
                    else:
                        continue
                        
                else:
                    cans[x][y]=count
                    q.append([x,y+1,count])
                    q.append([x+1,y,count])
                    
            else:
                if cans[x][y]==300 or count<cans[x][y]:
                    cans[x][y]=count
                    q.append([x,y+1,count])
                    q.append([x+1,y,count])
                else:
                    continue
                #print(ans)
     
search()
#for i in range(h):
 #   print(cans[i])9
           
print(cans[h-1][w-1]+asd)