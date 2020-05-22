import fractions
mod=10**9+7
n=int(input())
a=list(map(int,input().split()))

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

count=a[0]
for i in range(n-1):
    count=lcm(count,a[i+1])
ans=0
for i in range(n):
    ansa=count//a[i]
    ans+=ansa
    
print(ans%mod)
"""
mathtukae

"""