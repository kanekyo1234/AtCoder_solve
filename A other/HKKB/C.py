n = int(input())
p = list(map(int, input().split()))

jugh = [0]*200100
now = 0
for i in range(n):
    # print(jugh)
    jugh[p[i]] = 1
    if jugh[now] == 1:
        for j in range(now, 200100):
            if jugh[j] == 0:
                now = j
                break
    print(now)
