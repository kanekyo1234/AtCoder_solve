n = int(input())
x = input()
a = x.count("1")

for i in range(0, n):
    ans = 0
    x = list(x)
    if x[i] == "1":
        x[i] = "0"
        b = a-1
    else:
        x[i] = "1"
        b = a+1
    x = "".join(x)
    xatai = int(x, 2)
    while b != 0:
        xatai = xatai % b
        b = str(xatai).count("1")
        ans += 1
    print(ans)
    x = list(x)
    if x[i] == "1":
        x[i] = "0"
        b = a-1
    else:
        x[i] = "1"
        b = a+1
