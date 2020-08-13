l, h = map(int, input().split())
n = int(input())
a = [int(input()) for _ in range(n)]

for i in a:
    if i < l:
        print(l-i)
    elif h < i:
        print(-1)
    else:
        print(0)
