a, b, c = input().split()
a = int(a)-1
b = int(b)-1
x = 0
y = 0
if "R" in c:
    x = 1
if "L" in c:
    x = -1
if "U" in c:
    y = -1
if "D" in c:
    y = 1
s = [list(input()) for _ in range(9)]
ans = ""
if a == 0:
    x = 1
if a == 8:
    x = -1
if b == 8:
    y = -1
if b == 0:
    y = 1

for i in range(4):
    ans += s[b][a]
    a, b = a+x, b+y
    if a == 0 or a == 8:
        x *= -1
    if b == 0 or b == 8:
        y *= -1
print(ans)
