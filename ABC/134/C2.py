a=int(input())
b=[int(input()) for i in range(a)]
m=max(b) 

if b.count(m)>=2:
    for i in range(a):
        print (m)
else:
    c=b.copy()
    c.sort(reverse=True)
    m2=c[1]
    for i in range(a):
        if b[i]==m:
            print(m2)
        else:
            print (m)
