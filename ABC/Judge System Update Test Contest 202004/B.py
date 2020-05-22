n=int(input())
xc=[list(map(str,input().split())) for _ in range(n)]
#print(xc)
a=[]
b=[]
for i in range(n):
    if xc[i][1]=="R":
        a.append(int(xc[i][0]))
    else:
        b.append(int(xc[i][0]))

a.sort()
b.sort()
for i in range(len(a)):
    print(a[i])
for i in range(len(b)):
    print(b[i])

#print(xc)