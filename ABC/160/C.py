k,n=map(int,input().split())

a=list(map(int,input().split()))
ans=k-a[-1]+a[0]
#print(ans)
for i in range(n-1):
    ans=max(ans,-a[i]+a[i+1])

print(k-ans)



