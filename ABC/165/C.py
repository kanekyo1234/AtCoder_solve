import itertools
n,m,q=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(q)]
ac=tuple([i for i in range(1,m+1)])
ans=0
for A in list(itertools.combinations_with_replacement(ac,n)):
    count=0
    for j in range(q):
        if A[a[j][1]-1]-A[a[j][0]-1]==a[j][2]:
            count+=a[j][3]
    ans=max(ans,count)
print(ans)