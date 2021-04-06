n,k,s=map(int,input().split())
a=[]

for i in range(n):
    if (i+1)<=k:
        a.append(s)
    else:
        if s==10**9:
            a.append(10**9-1)
        else:
            a.append(10**9)



for i in range(n):
    print(a[i],end=" ")
