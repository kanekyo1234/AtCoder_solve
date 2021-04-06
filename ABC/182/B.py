
import math

n = int(input())

a = list(map(int, input().split()))

ans = 0
gcd_max = 0

for i in range(2, 1001):
    count = 0
    for j in a:
        if j % i == 0:
            count += 1
    if gcd_max <= count:
        ans = i
        gcd_max = count
print(ans)
