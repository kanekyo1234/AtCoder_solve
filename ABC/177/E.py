n = int(input())
a1 = list(map(int, input().split()))
k = 2
mod = 10**9 + 7


# pow(求めたいもの,-1,mod)でpython3.8.2ならできる
a = [1]  # i+1番目までの階乗
b = [1]  # a[i]の逆元

for i in range(1, n+1):
    a.append(a1[i-1] * a[i-1] % mod)
    b.append(pow(a[i], -1, mod))
print(a)
print(b)

# for i in range(2):

# for i in range(1, k+1):  # ../data_picture
#     if n-k < i-1:
#         print(0)
#     else:
#         blue_ball = k-i
#         blue_partition = i
#         blue_ans = a1[blue_ball + blue_partition - 1] * \
#             b[blue_ball] % mod * b[blue_partition-1] % mod
#         red_ball = n-k-i+1
#         red_partition = i+1
#         red_ans = a1[red_ball + red_partition - 1] * \
#             b[red_ball] % mod * b[red_partition-1] % mod
#         print((blue_ans * red_ans) % mod)
