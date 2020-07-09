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
        # print(rui[i], rui[left], k)
        left += 1

    ans += left
    # print(ans)

print(ans)


# for i in range(n):
#     goal += a[i]
#     if jugh == 0:
#         if k <= goal:
#             # print(goal)
#             ans += (n-i)
#             jugh = 1
#     if jugh == 1:
#         for j in range(start, i-start):
#             goal -= a[j]
#             if k <= goal:
#                 # print(goal)
#                 ans += 1
#             else:
#                 jugh = 0
#                 break
