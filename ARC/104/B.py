n, s = input().split()
ans = 0
n = int(n)
s = list(s)
for j in range(n):
    a_count = 0
    t_count = 0
    c_count = 0
    g_count = 0
    for i in range(j, n):
        if s[i] == "A":
            a_count += 1
        elif s[i] == "T":
            t_count += 1
        elif s[i] == "C":
            c_count += 1
        else:
            g_count += 1
        if a_count == t_count and c_count == g_count:
            ans += 1
print(ans)