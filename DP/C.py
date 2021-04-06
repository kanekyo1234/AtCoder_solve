n = int(input())
data = []
a=0
b=1
c=2
dp = [[0 for i in range(3)] for j in range(n)]
for i in range(n):
    data.append(list(map(int, input().split())))
dp[0][a]=data[0][a]
dp[0][b]=data[0][b]
dp[0][c]=data[0][c]
for i in range(1,n):
    #
    dp[i][a]=data[i][a]+max(dp[i-1][b],dp[i-1][c])
    dp[i][b]=data[i][b]+max(dp[i-1][a],dp[i-1][c])
    dp[i][c]=data[i][c]+max(dp[i-1][a],dp[i-1][b])
print(max(dp[-1][a],dp[-1][b],dp[-1][c]))


#二回目









n=int(input())

















