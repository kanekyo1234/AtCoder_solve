n,q=map(int,input().split())


a = [[0 for i in range(n)] for j in range(n)]

for z in range(q):
    count=[]
    d=list(map(int,input().split()))
    if d[0]==1:
        b=d[1]-1
        c=d[2]-1
        a[b][c]=1
    elif d[0]==2:
        b=d[1]-1
        for i in range(n):
            if a[i][b]==1:
                a[b][i]=1
        
    else:
        b=d[1]-1
        for i in range(n):
            if a[b][i]==1:
                count.append(i)
        for af in range(len(count)):
            for ad in range(n):
                if a[count[af]][ad]==1:
                    a[b][ad]=1

for i in range(n):
    for j in range(n):
        if i==j:
            print("N",end="")
        else:
            if a[i][j]==1:
                print("Y",end="")
            else:
                print("N",end="")
    print()
        

