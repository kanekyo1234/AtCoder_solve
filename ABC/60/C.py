n,k=map(int,input().split())

t=list(map(int,input().split()))
ans=k
for i in range(n-1):
    ans+=min(k,t[i+1]-t[i])
print(ans)