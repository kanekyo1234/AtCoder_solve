n, w = map(int, input().split())
stp = [list(map(int, input().split())) for i in range(n)]
imos = [0]*(10**5*2+1)
for i in range(n):
    s, t, p = stp[i]
    imos[s] += p
    imos[t] -= p
for i in range(1, len(imos)):
    imos[i] += imos[i-1]
if max(imos) > w:
    print("No")
else:
    print("Yes")
