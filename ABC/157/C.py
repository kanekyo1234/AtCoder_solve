n,m=map(int,input().split())


a=[]
for i in range(m):
    a.append(list(map(int,input().split())))


if m==0:
    if n==1:
        print(0)
    elif n==2:
        print(10)
    else:
        print(100)
    exit()

for i in range(m-1):
    for j in range(i+1,m):
        if a[i][0]==a[j][0]:
            if a[i][1]!=a[j][1]:
                print(-1)
                exit()

a.sort()
a1=10
a2=10
a3=10
if n==3:
    for i in range(m):
        if a[i][0]==1:
            a1=a[i][1]
        if a[i][0]==2:
            a2=a[i][1]
        if a[i][0]==3:
            a3=a[i][1]
    if a1==0:
        print(-1)
        exit()
    if a1==10:
        a1=1
    if a2==10:
        a2=0
    if a3==10:
        a3=0
    if (a1%10)*100+(a2%10)*10+(a3%10)==0:
        print(-1)
    else:
        print((a1%10)*100+(a2%10)*10+(a3%10))

elif n==2:
    for i in range(m):
        if a[i][0]==1:
            a1=a[i][1]
        if a[i][0]==2:
            a2=a[i][1]
    if a1==0:
        print(-1)
        exit()
    if a1==10:
        a1=1
    if a2==10:
        a2=0

    if (a1%10)*10+(a2%10)==0:
        print(-1)
    else:
        print((a1%10)*10+(a2%10)*1)

else:
    for i in range(m):
        if a[i][0]==1:
            a1=a[i][1]
    
    print(a1%10)
"""
ans=0
if a1!=10:
    ans+=a1*100
if a2!=10:
    ans+=a2*10
if a3!=10:
    ans+=a3


if ans==0:
    print(-1)
else:
    if n==2:
        ans=list(ans)
        for i in range(2):
            print(ans[i],end="")
    elif n==1:
        ans=list(ans)
        print(ans[0])
    else:
        print(ans)
"""