n = int(input())
x = list(map(int, input().split()))
ans1 = 0
ans2 = 0
ans3 = 0
for i in range(n):
    ans1 += abs(x[i])
    ans2 += abs(x[i])**2
    ans3 = max(ans3, abs(x[i]))
print(ans1)
print(ans2**0.5)
print(ans3)
