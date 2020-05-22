a,b=map(str,input().split())
ab=int(a+b)
if ab**0.5%1==0:
    print("Yes")
else:
    print("No")