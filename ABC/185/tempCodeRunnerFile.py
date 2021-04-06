n, m = map(int, input().split())
a = [0, n]+list(map(int, input().split()))
a = sorted(a, reverse=True)
# print(a)
difference = []

for i in range(len(a)-1):
    if a[i] - a[i+1]-1 > 0:
        difference.append(a[i] - a[i+1]-1)
if len(difference) != 0:
    k = min(difference)
    ans = 0
    for i in range(len(difference)):
        ans += (difference[i] // k + difference[i] % k)
    print(ans)
else:
    print(0)
