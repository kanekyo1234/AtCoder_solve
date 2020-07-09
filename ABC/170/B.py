x, y = map(int, input().split())
for i in range(0, x+1):
    if i*4+(x-i)*2 == y:
        print("Yes")
        break
else:
    print("No")
