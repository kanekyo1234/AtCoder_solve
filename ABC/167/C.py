
from itertools import  product
n,m,x=map(int,input().split())
ca=[list(map(int,input().split())) for _ in range(n)]
for i in range(1,m+1):
    count=0
    for j in range(n):
        count+=ca[j][i]
    if count<x:
        print(-1)
        exit()

ans=10**9



for z in product((0, 1), repeat=n):#bit全探索のくみあわせを勝手に作ってくれるので使うとよい
    count=0
    count2=[0]*m
    for i in range(n):
        if z[i]==1:
            count+=ca[i][0]
            for j in range(1,m+1):
                count2[j-1]+=ca[i][j]
    
    for i in range(m):
        if count2[i]<x:
            break
    else:
        ans=min(count,ans)
print(ans)
            

