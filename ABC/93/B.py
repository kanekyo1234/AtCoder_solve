a,b,k=map(int,input().split())

if k*2>(b-a+1):
    for i in range(a,a+b-a+1):
        print(i)
    print("SDFG")
else:
    for i in range(k):
        print(a+i)
    for i in range(k-1,-1,-1):
        print(b-i)

