
#二回目

n=int(input())
h=list(map(int,input().split()))

dp=[-1]*n
dp[0]=0
dp[1]=abs(h[1]-h[0])
for i in range(2,n):
    dp[i]=min(   abs(h[i]-h[i-1])+dp[i-1] ,abs(h[i]-h[i-2])+dp[i-2]  )
#print(dp)
print(dp[-1])




"""
#いっかいめ
n=int(input())
a=list(map(int,input().split()))

dp=[-1]*n
dp[0]=0
dp[1]=abs(a[0]-a[1])

for i in range(2,n):
    dp[i]=min(
        dp[i-2]+abs(a[i]-a[i-2]),
        dp[i-1]+abs(a[i]-a[i-1])
    )    
print(dp[-1])

"""