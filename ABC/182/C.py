from itertools import product
a = input()
n = len(a)
ans = 19
jugh = False
for z in product((0, 1), repeat=n):  # bit全探索のくみあわせ
    count = ""
    for i in range(n):  # ついてるスイッチと入力が正しいかの判定ループ
        if z[i] == 0:
            count += a[i:i+1]
    # print(count)
    if count == "":
        if int(a) % 3 == 0:
            ans = min(ans, sum(z))
        continue

    if int(count) % 3 == 0:
        ans = min(ans, sum(z))

if ans != 19:
    print(ans)
else:
    print(-1)
