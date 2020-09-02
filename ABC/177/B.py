s = list(input())
t = list(input())
ans = 0
for i in range(len(s)-len(t)+1):
    count = 0
    for j in range(len(t)):

        if s[j+i] == t[j]:
            count += 1
    ans = max(ans, count)

print(len(t)-ans)
