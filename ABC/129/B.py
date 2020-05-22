N=int(input())
W=list(map(int,input().split()))
 
sum1=0
ans=sum(W)
for i in range(N):
    sum1+=W[i]
    sum2=sum(W)-sum1
    count=abs(sum1-sum2)
    ans=min(count,ans)
print(ans)

