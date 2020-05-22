from collections import deque
n,q=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n-1)]
px=[list(map(int,input().split())) for _ in range(q)]

adlist=[]
finish=set()

point=[0]*n
for h in range(n):    
    adlist.append([])
for j in range(n-1):
    x=ab[j][0]
    y=ab[j][1]
    adlist[x-1].append(y)
    adlist[y-1].append(x)
for i in range(q):
    point[px[i][0]-1]+=px[i][1]
#print(point)
deq=deque()
deq.append(1)


while deq:
    now=deq.pop()
       # print(now)
    finish.add(now)
    for i in range(len(adlist[now-1])):
        #print(adlist[now-1][i],now)
        if adlist[now-1][i] not in finish:
            point[adlist[now-1][i]-1]+=point[now-1]
            deq.append(adlist[now-1][i])

for i in range(n):
    print(point[i],end=" ")

"""
finish=set()
finish.add(1)
#print(adlist)
dfs(1,finish)#引数がけすノード
print(ans)"""