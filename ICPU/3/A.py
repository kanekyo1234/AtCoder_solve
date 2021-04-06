ans = []
while True:
    a, b, c = map(int, input().split())
    if a+b+c == 0:
        for i in range(len(ans)):
            print(ans[i])
        break

    print(int(c/((100+a)/100)))
