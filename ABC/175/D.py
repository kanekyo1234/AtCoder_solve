n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = []
count2 = []
for i in range(n):
    ans2 = []
    syote = i
    count = 0
    for j in range(min(k, n)):
        count += c[p[syote]-1]
        ans2.append(count)
        syote = p[syote]-1
    count2.append(count)
    ans.append(max(ans2))
aaa = max(ans)
if k <= n:
    print(aaa)
# else:
#     kaisuu = k//n
#     amari = k % n

#     ans4 = []
#     count2 = []
#     for i in range(n):
#         ans2 = []
#         syote = i
#         count = 0
#         for j in range(amari):
#             count += c[p[syote]-1]
#             ans2.append(count)
#             syote = p[syote]-1
#         count2.append(count)
#         ans4.append(max(ans2))
#         print(ans4)
#     print(ans)
#     for i in range(len(ans)):
#         ans[i] *= kaisuu
#         ans[i] += ans4[i]
#     print(max(ans))
