h,w=map(int,input().split())



if (h*w)%5==0:
    print("Yes")
    for i in range(h):
        for i in range(w):
            print("5",end="")

elif (h*w)%2==0:
    print("Yes")
    for i in range(h):
        for i in range(w):
            print("2",end="")

else:
    print("No")