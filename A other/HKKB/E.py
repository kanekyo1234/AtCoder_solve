h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
mod = 1000000007
k = 0
for i in range(h):
    count = 0
    now = 0
    for j in range(w):
        if s[i][j] == "#":
            s[i][j-1] = count
            now = j+1
            count = 0
        else:
            count += 1
            k += 1
    if s[i][j] != "#":
        s[i][j] = count
    for j in range(w-1, -1, -1):
        if s[i][j] == ".":
            s[i][j] = count
        elif s[i][j] == "#":
            count = 0
        else:
            count = s[i][j]
        s[i][j] = count
print(s)
for j in range(w):
    count = -1
    now = 0
    for i in range(h):
        if s[i][j] == "#":
            for x in range(now, i):
                s[x][j] += count
            now = i+1
            count = -1
        else:
            count += 1
    for x in range(now, h):
        s[x][j] += count


# print(s, k)
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] != "#":
            ans += 2**k-2**(k-s[i][j])
            ans %= mod
            # print(ans)


print(ans % mod)
