h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
k = 0
for i in range(h):
    count = 0
    start = 0
    end = 0
    for j in range(w):
        if s[i][j] != "#":  # 　#じゃなければおけ
            count += 1
            k += 1
        else:
            for z in range(start, end):
                s[i][z] = count
            start = end+1
            count = 0
        end += 1
    for z in range(start, end):
        s[i][z] = count
    # print(s[i])
ans = 0

for i in range(w):
    count = -1
    start = 0
    end = 0
    for j in range(h):
        if s[j][i] != "#":  # 　#じゃなければおけ
            count += 1
        else:
            for z in range(start, end):
                s[z][i] += count
            start = end+1
            count = -1
        end += 1
    for z in range(start, end):
        s[z][i] += count
# print()
mod = 1000000007
# print(s, k)

ans = pow(2, k, mod)*k %mod
for i in range(h):
    for j in range(w):
        if s[i][j] != "#":
            ans = (ans-pow(2,k-s[i][j],mod))
            # ans %= mod
            # print(ans)


print(ans % mod)
