a = int(input())
s = input()
ans = 0
ss = s.count("R")
for i in range(ss, a):
    if s[i] == "R":
        ans += 1
print(ans)
