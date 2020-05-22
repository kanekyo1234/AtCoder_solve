s=list(str(input()))
t=list(str(input()))

dp=[[0]*(len(t)+1) for _ in range(len(s)+1) ]
#print(dp)
for i in range(1,len(t)+1):
    for j in range(1,len(s)+1):
        if t[i-1]==s[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
 #   print(dp)
#for i in range(len(s)+1):
 #   print(dp[i])
print(dp[len(s)][len(t)]+1)
"""
s = list(input())
t = list(input())
n = len(s)
m = len(t)
ans = 0
dp = [[0]*(m+1) for j in range(n+1)]
print(dp)
for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
for i in range(len(s)+1):
    print(dp[i])
print(dp[n][m]+1)

"""