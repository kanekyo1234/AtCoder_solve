n,m=map(int,input().split())
mod=10**9+7
t=[int(input()) for i in range(m)] 
dp=[-1]*(n+1)

dp[0]=1 #0が１なのは２段目の回答を合わせるためdp[０]＝０、dp[1]=0,ds[2]=1
#は入力が1,0のきエラーになるので、だめ
dp[1]=1
for i in range(m):
    dp[t[i]]=0#ここはそもそもいけないので０になる


for i in range(2,n+1):
    if dp[i]==-1:
        dp[i]=dp[i-1]+dp[i-2]#このばしょにくるほうほうは二個前からくるか一個前からくるか、そこのあたいをたっせばいい
print(dp[-1]%mod)
