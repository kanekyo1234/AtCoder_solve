x, n = map(int, input().split())
p = list(map(int, input().split()))
ans = 1000
jugh = 1000
for i in range(0, 150):
    if abs(x-i) < jugh and i not in p:
        jugh = abs(x-i)
        ans = i
    # print(ans)
print(ans)
