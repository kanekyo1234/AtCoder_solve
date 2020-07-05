n=int(input())
a=list(map(int,input().split()))
ans=1
count=1
"""
for i in range(1,n+1):
    ans+=count*2
    count*=2
#print(ans)
"""
ans=1
count=1
now=1
for i in range(n+1):
    if i==0:
        count=(count-a[i])*2
        ans+=count
        continue
    count=(count-a[i])*2
    if a[i]%2==1:
        now=now*2-a[i]-1
    else:
        now=now*2-a[i]
    ans+=count
    count=now
    print(count,ans,now)

print(max(-1,ans))