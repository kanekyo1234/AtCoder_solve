k = int(input())
n = 10**6
a = 0
for i in range(n):
    a *= 10
    a += 7
    a = a % k
    if a == 0:
        print(i+1)
        break


else:
    print("-1")


# k = int(input())
# n = 10**6
# b = "7"
# if k % 2 == 0:
#     print(-1)
#     exit()
# for i in range(1, n):
#     a = list(set(str(k*i)))
#     # print(a, k*i)
#     if len(a) == 1 and a[0] == "7":
#         print(len(str(k*i)))
#         break
# else:
#     print(-1)

# print()
