t = int(input())
ans = []
for i in range(t):
    a, b = map(int, input().split())
    if a*2 > b:
        ans.append(0)
    else:
        count = 0
        b -= a*2
        if b % 2 == 1:
            ans.append((b+1)*(b//2+1)+b//2+1)
        else:
            ans.append((b+1)*(b//2+1))
        # for i in range(1, b+1+1):
        #     count += i
        # ans.append(count)
for i in ans:
    print(i)
# print(ans)
