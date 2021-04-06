import itertools
ans = 0
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
for i in list(itertools.permutations(range(1, n))):
    now = 0
    count = 0
    for j in i:
        count += t[now][j]
        now = j

    if count+t[now][0] == k:
        ans += 1
print(ans)
