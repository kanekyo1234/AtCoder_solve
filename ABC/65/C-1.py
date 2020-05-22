n,m=map(int,input().split())
if 2<=abs(n-m):
    print(0)
    exit()
mod=10**9+7

if abs(n-m)==1:
    dog=1
    cat=1
    for i in range(1,n+1):
        dog*=i
        dog=dog%mod
    for i in range(1,m+1):
        cat*=i
        cat=cat%mod
    print(dog*cat%mod)
else:
    dog=1
    cat=1
    for i in range(1,n+1):
        dog*=i
        dog=dog%mod
    for i in range(1,m+1):
        cat*=i
        cat=cat%mod
    print(dog*cat*2%mod)


