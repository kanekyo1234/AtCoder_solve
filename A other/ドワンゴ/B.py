import copy
mod=10**9+7
n=int(input())
x=list(map(int,input().split()))
ans=0
a=x.copy()
for i in range(n-1):
    x=a.copy()
    for i in range(n-1):
        ran=
        ans+=(x[ran+1]-x[ran])
        x.pop(ran)
    print(x)
print(ans%mod)
