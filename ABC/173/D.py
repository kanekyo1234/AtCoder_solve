n = int(input())
a = list(map(int, input().split()))

a = sorted(a, reverse=True)
ans = a[0]

for i in range((n-2)//2):
    ans += a[i+1]*2
    # print(ans)
if (n) % 2 == 1:
   # print(a[i+2], i+2)
    ans += a[i+2]
print(ans)
