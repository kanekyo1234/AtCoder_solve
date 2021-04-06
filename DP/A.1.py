n=int(input())
a=list(map(int,input().split()))

dp=[-1]*n
dp[0]=0
dp[1]=abs(a[0]-a[1])

for i in range(2,n):
    dp[i]=min(abs(a[i]-a[i-2]),abs(a[i]-a[i-1])+abs(a[i-2]-a[i-1]))

print(dp)
"""
dpに何が入っているのかを整理すること
この問題を間違えた原因は考える必要のない計算をしていること
"""