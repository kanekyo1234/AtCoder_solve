n,x=map(int,input().split())
a=list(map(int,input().split()))
x=list(str(bin(x))[2:])[::-1]
ans=0
for i in range(len(x)):
    ans+=a[i]*int(x[i])
print(ans)