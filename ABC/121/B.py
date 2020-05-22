n,m,c=map(int,input().split())
b=list(map(int,input().split()))
a=[list(map(int,input().split())) for i in range(n)]

sum1=0
ans=0
for i in range(n):
    for j in range(m):
        sum1+=a[i][j]*b[j]
    sum1+=c
    if sum1>0:
        ans+=1
    sum1=0
print(ans)