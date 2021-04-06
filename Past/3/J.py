n,m=map(int,input().split())
a=list(map(int,input().split()))
now=[]
for i in range(m):
    aaa=len(now)
    for j in range(aaa-1,-1,-1):
        if now[j]>a[i]:
            now[j-1]=a[i]
            print(j)
            break
    else:
        if aaa!=n:
            now.append(a[i])
            print(aaa)
        else:
            print(-1)    
    