n,m=map(int,input().split())
a=list(map(int,input().split()))
ma=sum(a)
#print(ma)
if ma<=n:
    print(n-ma)
else:
    print(-1)