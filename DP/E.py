n,W=map(int,input().split())

w=[0]*(n+1)
v=[0]*(n+1)
sum_v=0
#価値を全部足したうえで考えれば10**3*10**2*10**2で間に合う
for i in range(n):
    a,b=list(map(int,input().split()))
    w[i+1]=a
    v[i+1]=b
    sum_v+=b
#print(sum_v)
dp= [[10**9 for i in range(sum_v+1)] for j in range(n+1)]
#for i in range(n):
 #   print(dp[i])
dp[0][0]=0
for i in range(1,n+1):
    for j in range(sum_v+1):
        if j>=v[i]:
            dp[i][j]=min(dp[i-1][j-v[i-1]] + w[i-1] , dp[i-1][j])  
        else:
            dp[i][j]=dp[i-1][j]
print(dp[i])
print(dp[-1][-1])