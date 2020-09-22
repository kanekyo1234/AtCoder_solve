a = int(input())
ans = 0
for i in range(1, a):
    ans += a//i
    if a % i == 0:
        ans -= 1
    # print(i, ans)
print(ans)
