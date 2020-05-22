n=int(input())
a=list(map(int,input().split()))
ans=10**9
ab=0
for i in range(-100,101):
    count=0
    for j in range(n):
        count+=abs(a[j]-i)**2
    if ans>count:
        ans=count
        ab=i
print(ans)