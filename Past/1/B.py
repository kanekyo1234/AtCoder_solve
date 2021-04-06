n=int(input())
a=[int(input()) for i in range(n)]

for i in range(1,n):
    if a[i-1]<a[i]:
        print("up",end=" ")
        print(abs(a[i]-a[i-1]))
    elif a[i-1]>a[i]:
        print("down",end=" ")
        print(abs(a[i]-a[i-1]))
    else:
        print("stay")
