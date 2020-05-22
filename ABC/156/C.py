n=int(input())
x=list(map(int,input().split()))

#print(a)
ans=10**100
for j in range(1,101):
    ans2=0
    for i in range(n):
        ans2+=(x[i]-j)**2
    ans=min(ans,ans2)

print(ans)
