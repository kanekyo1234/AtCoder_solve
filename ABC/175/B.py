n = int(input())
ans = 0
l = list(map(int, input().split()))
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for z in range(j+1, n):
            ma = max(l[i], l[j], l[z])
            mi = min(l[i], l[j], l[z])
            mm = (l[i] + l[j] + l[z])-ma-mi
            if mm-mi < ma and ma < mi+mm and l[i] != l[j] and l[j] != l[z] and l[i] != l[z]:
                ans += 1
                # print(i, j, z)

print(ans)
