a, b, c = map(int, input().split())
k = int(input())
ans = 0
for i in range(10000):
    if a < b and b < c:
        break
    else:
        if a < b:
            c *= 2

        else:
            b *= 2

    ans += 1

if ans <= k:
    print("Yes")
else:
    print("No")
