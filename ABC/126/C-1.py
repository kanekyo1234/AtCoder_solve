n,k=map(int,input().split())
ans=0
for i in range(1,n+1):
    count=0
    now=i
    if i<k:
        while now<k:
            now*=2
            count+=1
        ans+=0.5**count
    else:
        ans+=1



print(ans/n)