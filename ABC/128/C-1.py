from itertools import  product
n,m=map(int,input().split())
s=[]
for i in range(m):
    s.append(list(map(int,input().split())))
p=list(map(int,input().split()))
ans=0

for z in product((0, 1), repeat=n):
    righton_count=0
    for i in range(m):
        switc_on_count=0
        for j in range(1,s[i][0]+1):
            if z[s[i][j]-1]==1:              
                switc_on_count+=1
        if switc_on_count%2==p[i]:
            righton_count+=1
    if righton_count==m:
        ans+=1



print(ans)