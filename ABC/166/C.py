n,m=map(int,input().split())
h=list(map(int,input().split()))

ab=[list(map(int,input().split())) for _ in range(m)]

ans=[0]*n

count =[[h[i]] for i in range(n)]
#print(count) 
for i in range(m):
    count[ab[i][0]-1].append(h[ab[i][1]-1])
    count[ab[i][1]-1].append(h[ab[i][0]-1])
#print(count)
ans=[]
for i in range(n):
    if h[i]==max(count[i]) and count[i].count(h[i])==1:
        ans.append(max(count[i]))
#print(ans)
print(len(set(ans)))
