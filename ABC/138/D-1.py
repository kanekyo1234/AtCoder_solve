from collections import deque
n, q = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n-1)]
px = [list(map(int, input().split())) for i in range(q)]
ans = [0]*n
adlist = [[] for i in range(n)]
for i in range(q):
    ans[px[i][0]-1] += px[i][1]
for i in range(n-1):
    x, y = ab[i]
    adlist[x-1].append(y)
    adlist[y-1].append(x)
# print(adlist)
print(ans)
deq = deque()  # まだ見ていない場所をメモするところ
deq.append(1)  # １を見るっていうメモを残す
finish = set()
while deq:
    print(deq)
    now = deq.popleft()  # 見てる場所
    finish.add(now)
    for i in range(len(adlist[now-1])):
        line = adlist[now-1][i]
        # print(line)
        if line not in finish:
            deq.append(line)
            ans[line-1] += ans[now-1]

print(*ans)
