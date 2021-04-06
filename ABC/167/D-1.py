n, k = map(int, input().split())
a = list(map(int, input().split()))
was = set()
now = 0
count = 0

if n >= k or 1000000 >= k:
    for i in range(k-1):
        now = a[now]-1
    print(a[now])
    exit()


for i in range(n):
    if a[now] in was:
        # print(was, a[now], now+1, count)
        box = now
        now = a[now]-1
        k -= count
        count2 = 0
        for i in range(n):
            if box == a[now]:
                break
            else:
                now = a[now]-1
                count2 += 1
        k -= 1
        k %= count2
        # print(k)
        was = list(was)
        print(was[k-1])

        break
    else:
        was.add(a[now])
        now = a[now]-1
        count += 1
