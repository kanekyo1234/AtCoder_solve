n, x, m = map(int, input().split())
ans = x
aaa = 0
a = []
syuuki = 0
count = 0
for i in range(min(n, m)-1):
    ans += (x**2) % m
    # print(ans, (x**2) % m)
    x = x**2
    x %= m
    if x == 0:
        aaa = 1
        # print(i)
        break
    if x in a:
        if count == 0:
            for j in range(len(a)):
                if x == a[j]:
                    syuuki = i-j
                    count = 1

    else:
        if count == 0:
            a.append(x)

print(syuuki, len(a))

# # print(492443256176507)
# print(ans)
# if aaa == 1:
#     print(ans)
# else:
#     if n > m:
#         print(ans*(10000000000//99959))
#         ans *= n//m+n % m
#     #     for i in range(n % m):
#     #         ans += (x**2) % m
#     # # print(ans, (x**2) % m)
#     #         x = x**2
#     #         x %= m
#     #         if x == 0:
#     #             aaa = 1
#     #             print(i)
#     #             break
#         print(492443256176507)
#         print(ans)
