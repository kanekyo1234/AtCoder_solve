n = int(input())
s = [input() for i in range(n)]

a = 0
b = 0
c = 0
d = 0

for i in range(n):
    if s[i] == "AC":
        a += 1
    if s[i] == "WA":
        b += 1
    if s[i] == "TLE":
        c += 1
    if s[i] == "RE":
        d += 1

print("AC x", a)
print("WA x", b)
print("TLE x", c)
print("RE x", d)
