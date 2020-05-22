a,b,c=map(int,input().split())
m=max(a,b,c)*3
f=a+b+c
if (m-f)%2==0:
    print((m-f)//2)
else:
    print((m-f)//2+2)