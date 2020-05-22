
import math

mod=10**9+7
n=int(input())
x=list(map(int,input().split()))

kai=math.factorial(n-1)
a=[]
for i in range(n-1):
    a.append(x[i+1]-x[i])
ans=0
count=0
a1=sum(a)
for i in range(n-1):
    count+=kai/(i+1)
    ans+=a[i]*count
print(int(ans%mod))