x, y, a, b = map(int, input().split())
ans = 0
while True:
    if x*a-x >= b:
        break
    else:
        if x*a < y:
            x *= a
            ans += 1
        else:
            break

# print(ans)
if (y-x) % b == 0:
    ans += (y-x)//b-1
else:
    ans += (y-x)//b
print(ans)
