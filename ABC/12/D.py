# https://juppy.hatenablog.com/entry/2018/11/01/%E8%9F%BB%E6%9C%AC_python_%E5%85%A8%E7%82%B9%E5%AF%BE%E6%9C%80%E7%9F%AD%E7%B5%8C%E8%B7%AF%E6%B3%95%EF%BC%88%E3%83%AF%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E6%B3%95
# ワーシャルフロイド法　全点体最短経路　pypyなら通る
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


##############################
n, m = map(int, input().split())  # n:頂点数　w:辺の数

d = [[float("inf")]*n for i in range(n)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(m):
    x, y, z = map(int, input().split())
    d[x-1][y-1] = z
    d[y-1][x-1] = z
for i in range(n):
    d[i][i] = 0  # 自身のところに行くコストは０
data = warshall_floyd(d)
# print(data)
ans = []
for i in range(n):
    count = []
    for j in range(n):
        count.append(d[j][i])
    ans.append(max(count))
print(min(ans))
