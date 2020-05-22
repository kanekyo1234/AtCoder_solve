n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)
a.insert(n+1,0)
b=[0]*(n+1)

for i in range(n+1):
    b[i]=abs(a[i]-a[i+1])
ans=sum(b)
#print(a,b)
for i in range(n):
    #print(ans,b[i],b[i+1],abs(a[i]-a[i+2]))
    print(ans-b[i]-b[i+1]+abs(a[i]-a[i+2]))

