import collections
n,m=map(int,input().split())
a=list(map(int,input().split()))
a=collections.Counter(a)
ans='?'
for s,v in a.items():
    if n//2<v:
        ans=s
        break
print(ans)

