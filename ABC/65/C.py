import math
mod = 10**9+7
n,m = map(int,input().split())
if n!=m and abs(n-m)!=1:
    print("0")
    exit()

if n==m:
    n=max(n,m)
    m=min(n,m)
    ans = math.factorial(n)*2*math.factorial(m)
    print(ans%mod)
else:
    ans = math.factorial(n)*math.factorial(m)
    print(ans%mod)

