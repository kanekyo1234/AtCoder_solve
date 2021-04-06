mod=10007
n=int(input())
dp=[-1]*(n+4)
dp[0]=0
dp[1]=0
dp[2]=0
dp[3]=1

for i in range(4,n+4):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    dp[i]%=mod
"""
def fibo(n):
    if dp[n]!=-1:
        return dp[n]
    else:
        dp[n]=  fibo(n-1) + fibo(n-2) + fibo(n-3)
        dp[n]=dp[n]%mod
        return dp[n]
fibo(n)
"""
print(dp[-4])
