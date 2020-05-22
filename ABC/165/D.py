import math
a,b,n=map(int,input().split())
ans=min(n,b-1)
print(math.floor(a*ans/b)-math.floor(ans/b))
