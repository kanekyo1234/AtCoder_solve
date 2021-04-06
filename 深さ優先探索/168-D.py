from collections import deque
n,m=map(int,input().split())

ab=[list(map(int,input().split())) for _ in range(m)]
ans=[0]*n

def dfs():
    deq.append(0)#1
    finish=set()
    finish.add(0)
    while deq:
        now=deq.popleft()
     #   print(now+1)
        for ad_i in adlist[now]:
            if ad_i-1 != now and ad_i-1 not in finish:
                if ans[ad_i-1]==0:
                    ans[ad_i-1]=now+1
                deq.append(ad_i-1)
                finish.add(ad_i-1)
deq=deque()
dfs()
print("Yes")
for i in range(1,n):
    print(ans[i])
    