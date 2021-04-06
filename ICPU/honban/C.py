# ans = []


# def make_divisors(n):
#     lower_divisors, upper_divisors = [], []
#     i = 1
# #     while i*i <= n:
# #         if n % i == 0:
# #             lower_divisors.append(i)
# #             if i != n // i:
# #                 upper_divisors.append(n//i)
# #         i += 1
# #     return lower_divisors + upper_divisors[::-1]


# # n = 10**14
# # print(len(make_divisors(n)))
# from math import ceil
# ans = []


# def calc(n):
#     cnt = n + 2
#     for i in range(ceil(n ** (1 / 3)), ceil(n ** 0.5) + 1):
#         if n % i == 0:
#             for j in range(1, ceil((n / i) ** (0.5)) + 1):
#                 k = n / (i * j)
#                 if k == int(k) and cnt >= i + j + k:
#                     cnt = i + j + k
#     return int(cnt)


# while True:
#     n = int(input())
#     if n == 0:
#         break
#     ans.append(calc(n))
# for i in ans:
#     print(i)

import sympy

ans = []
while True:
    n = int(input())
    ans2 = n+3
    if n == 0:
        break
    yakusuu = sympy.divisors(n)
    if len(yakusuu) == 2:
        ans.append(n+2)
        break

    for i in yakusuu:
        if i**3 == n:
            ans2 = min(ans2, i*3)
            break
        if i**2 == n:
            yakusuu = sympy.divisors(n)
            ans2 = min(ans2)
        else:

    ans.append(ans2)


for i in ans:
    print(i)
