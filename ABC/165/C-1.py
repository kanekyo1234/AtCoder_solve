n,m,q=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(q)]

ans=0
for i in range(0,q,2):
    ans+=a[i][3]
print(ans)