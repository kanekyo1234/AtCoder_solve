s = list(input())
count = 1
r_count = 1
l_count = 0
was = 0
ans = [0]*len(s)
for i in range(1, len(s)):
    if s[i-1] == "L" and s[i] == "R":
        # print(count, r_count, l_count)
        now = r_count+was
        if count % 2 == 0:
            ans[now-1] = count//2
            ans[now] = count//2
        else:
            if r_count % 2 == 0:  # Rが偶数
                ans[now-1] = count//2
                ans[now] = count//2+1
            else:
                ans[now-1] = count//2+1
                ans[now] = count//2

        count = 1
        r_count = 1
        l_count = 0
        was = i
    else:
        if s[i] == "R":
            r_count += 1
        else:
            l_count += 1
        count += 1
now = r_count+was
if count % 2 == 0:
    ans[now-1] = count//2
    ans[now] = count//2
else:
    if r_count % 2 == 0:  # Rが偶数
        ans[now-1] = count//2
        ans[now] = count//2+1
    else:
        ans[now-1] = count//2+1
        ans[now] = count//2
print(*ans)
