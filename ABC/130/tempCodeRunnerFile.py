n, k = map(int, input().split())
a = list(map(int, input().split()))
rui = [0]
for i in range(0, n):
    rui.append(rui[i]+a[i])
# print(rui)
# right = 0
left = 0
# now = 0
ans = 0

for i in range(n+1):

    while k <= rui[i]-rui[left]:
        print(rui[i], rui[left], k)
        left += 1

    ans += left
    # print(ans)

print(ans)
