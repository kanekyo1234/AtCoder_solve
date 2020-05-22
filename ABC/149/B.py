a,b,k=map(int,input().split())
if k<a:
    print(a-k,end=" ")
    print(b)
else:
    if k-a<b:
        print("0",end=" ")
        print(b-(k-a))

    else:
        print("0 0")