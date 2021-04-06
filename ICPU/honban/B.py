ans = []

while True:
    m, n, p = map(int, input().split())
    if m+n+p == 0:
        break
    ab = [list(map(int, input().split())) for _ in range(n)]

    kansen = set()
    kansen.add(p)
    for i in range(n):
        a = ab[i][0]
        b = ab[i][1]
        if a in kansen or b in kansen:
            kansen.add(a)
            kansen.add(b)
    ans.append(len(kansen))
for i in ans:
    print(i)
