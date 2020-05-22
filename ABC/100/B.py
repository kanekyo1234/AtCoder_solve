d,n=map(int,input().split())
if n==100:
    if d==0:
        print("101")
    elif d==1:
        print("10100")
    else:
        print("1010000")
else:
    print(100**d*n)
