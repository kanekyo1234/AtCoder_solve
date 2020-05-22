a=int(input())
b=[int(input()) for i in range(a)] 
c=0
for i in range(len(b)):
    c=b
    c[i]=0
    c.sort()
    print (c)
    print(b)
    print (c[len(c)-1])
    c=0