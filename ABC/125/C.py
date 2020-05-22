import math
from functools import reduce
n=int(input())
a=list(map(int,input().split()))


l=[0]
r=[0]
for i in range(0,n):
    l.append(math.gcd(l[i],a[i]))
    r.append(math.gcd(r[i],a[n-i-1]))

print(l,r)
r=r[::-1]
ans=[]
for i in range(n):
    ans.append(math.gcd(l[i],r[i+1]))
print(ans)
print(max(ans))
"""
import math
 
 
N = int(input())
A = list(map(int, input().split()))
 
gcd_l = [0]
gcd_r = [0]
for i in range(N):
    gcd_l.append(math.gcd(gcd_l[i], A[i]))
    gcd_r.append(math.gcd(gcd_r[i], A[-(i+1)]))
print(gcd_l)
"""