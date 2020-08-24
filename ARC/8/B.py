import collections
n, m = map(int, input().split())
name = input()
kit = input()
namecount = collections.Counter(name)
kitcount = collections.Counter(kit)
# print(namecount)
for i in range(1, 52):
    for v, k in kitcount.items():
        if v in namecount:
            namecount[v] -= k
    for v in namecount.values():
        if v > 0:
            break
    else:
        break
else:
    print(-1)
    exit()
print(i)
