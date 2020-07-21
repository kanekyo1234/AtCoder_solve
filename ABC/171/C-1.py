n = int(input())

ans = ""

for i in range(1, 15):
    if n <= 26**i:
        # print(n)
        n -= 1
        for j in range(i):
            ans = chr(ord("a") + n % 26) + ans
            # print(ans)
            n //= 26
        break
    else:
        n -= 26**i

print(ans)
