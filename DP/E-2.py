# 三回目

n, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
first = 10**10
value_sum = 0  # 価値の最大値はvi*n=1000*100
for i in range(n):
    value_sum += wv[i][1]

value_sum += 1  # 一応
# dp[2][5]2番目までの商品を5以上の価値にするように選ぶ時の最小の重さって感覚
# この＋１は0番目（リストの中身は全部0)というのが欲しかったのと実際の値とずれるから
dp = [[first]*(value_sum) for _ in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
    w = wv[i-1][0]
    v = wv[i-1][1]

    for j in range(value_sum):
        if v <= j:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v]+w)
        else:  # j以上にするんだからjより大きかったらする意味ないよね
            dp[i][j] = dp[i-1][j]
ans = 0

# for i in range(n+1):
#     print(dp[i])

for i in range(n+1):
    for j in range(value_sum):
        if dp[i][j] != 10**10 and dp[i][j] <= W:
            ans = max(ans, j)
print(ans)
