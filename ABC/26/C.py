n=int(input())

b=[[i] for i in range(2,n+1)]
for i in range(n-1):
    a=int(input())
    b[i].append(a)
    b[i].append(1)

#print(b)
jugh=0
for j in range(n,0,-1):#
    count=[]
    for i in range(0,n-1):
        if b[i][1]==j:
            jugh=1
            count.append(b[i][2])
    if jugh==1:
        jugh=0
        b[j-2][2]+=max(count)+min(count)
    #print(count,j)
#print(b)
print(b[-1][2])

