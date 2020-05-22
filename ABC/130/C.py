a,b,x,y=map(int,input().split())

tx=a/2
ty=b/2

print(a*b/2,end= " ")
if(tx==x and ty==y):
    print("1")
else:
    print("0")
