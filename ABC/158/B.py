n,a,b=map(int,input().split())
d=a+b
ans=n//d*a

ans+=min(a,n%d)
print(ans)
