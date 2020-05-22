n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=0
count=0
for i in range(k):
    count+=a[i]
ans=count
for i in range(0,n-k):
    count=count-a[i]+a[i+k]
    ans+=count
    #print(ans,count)
print(ans)

