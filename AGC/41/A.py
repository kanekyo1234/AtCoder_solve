n,a,b=map(int,input().split())
if (a+b)%2==1: 
    if (n-b)>(a-1):
        print(a+(b-a-1)//2)
    else:
        print(((n-b)+1)+(b-a-1)//2)
else:
    print((b-a)//2)