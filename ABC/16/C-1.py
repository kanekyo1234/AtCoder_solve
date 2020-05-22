from collections import deque
n,m=map(int,input().split())
ab=[]
for i in range(m):
    ab.append(list(map(int,input().split())))
ans=0
def dfs(i):
    deq.append((i,1))#1
    finish=set()
    finish.add(i)
    ans=[0]*n #距離
    while deq:
        now,distance=deq.popleft()
       # print(now+1)
        for ad_i in adlist[now]:
            if ad_i-1 != now and ad_i-1 not in finish:
                ans[ad_i-1]=distance
                deq.append((ad_i-1,distance+1))
                finish.add(ad_i-1)
    #print(ans)
    return ans.count(2)
    

adlist=[]
for h in range(n):    
    adlist.append([])
for j in range(m):
    x=ab[j][0]
    y=ab[j][1]
    adlist[x-1].append(y)
    adlist[y-1].append(x)
deq=deque()
for i in range(n):
    print(dfs(i))

#print(adlist)

#print(ans)