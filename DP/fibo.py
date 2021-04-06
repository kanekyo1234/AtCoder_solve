
dp=[-1]*1000
dp[0]=0
dp[1]=1
def fibo(n):
    if dp[n]!=-1:
        return dp[n]
    else:
        dp[n]=  fibo(n-1) + fibo(n-2)
        return dp[n]
print(fibo(10000))
