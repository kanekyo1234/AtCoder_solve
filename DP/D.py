n,w=map(int,input().split())
weight=[]
money=[]
weight.append(0)
money.append(0)
for i in range(n):
    s,v=map(int,input().split())
    weight.append(s)
    money.append(v)
dp= [[-1 for i in range(w+1)] for j in range(n+1)]
for i in range(w+
1):
    dp[0][i]=0

for i in range(1,n+1):
    for j in range(1,w+1):
        if j>=weight[i]:
            dp[i][j]=max(dp[i-1][j-weight[i]] + money[i],dp[i-1][j])  
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])