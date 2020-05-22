import math
n=int(input())
t=[int(input()) for _ in range(n)]

n=int(input())
t=[int(input()) for _ in range(n)]
ans = t[0]
for i in range(1, n):
    ans = ans * t[i] // math.gcd(ans, t[i])
print(ans)
"""

import fractions

n=int(input())
t=[int(input()) for _ in range(n)]
ans = t[0]
for i in range(1, n):
    ans = ans * t[i] // fractions.gcd(ans, t[i])
print(ans)
"""