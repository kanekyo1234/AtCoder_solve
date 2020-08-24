a = list(str(input()))
count = 0
ans = 0
for i in range(3):
    if a[i] == "R":
        count += 1
    else:
        ans = max(ans, count)
        count = 0
ans = max(ans, count)

print(ans)
