a = int(input())
ans = 8
for i in range(400, 12111, 200):

    if i <= a and a < i+200:
        print(ans)
        break
    ans -= 1
