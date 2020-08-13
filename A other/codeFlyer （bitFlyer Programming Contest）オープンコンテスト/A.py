n = int(input())
p = [input() for _ in range(n)]
ans = []

for i in range(n):
    count = 0
    for j in range(len(p[i])-1, -1, -1):
        a = p[i]
        # print(a[j])
        if int(a[j]) == 0:

            count += 1
        else:
            break
    ans.append(count)
# print(ans)
print(min(ans))
