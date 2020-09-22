n, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(k)]

dp = [0]*(n+1)
for i in range(k):
    for j in range(lr[i][0], lr[i][1]+1):
        dp[j] = 1
print(dp)
for i in range(1, n+1):
    dp[i] += dp[i-1]

print(dp)


# while
