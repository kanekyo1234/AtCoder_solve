n=int(input())
ans=0
for i in range(1,n+1):
    ans+=i
    if i%3==0 or i%5==0 or i%15==0:
        ans-=i
    #print(ans)
print(ans)
