N = int(input())
H = list(map(int, input().split()))
v = -1
for h in H:
    if v > h:
        if v != h+1:
            print("No")
            exit()
        else:
            v = h+1
    else:
        v = h
print("Yes")
