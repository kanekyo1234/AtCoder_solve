n,m,q=map(int,input().split())

ab=[]
for i in range(m):
    ab.append(list(map(int,input().split())))

adlist=[ [] for i in range(n)]#交流のあるやつ同士の隣接リスト
for i in range(m):#1から順に見ていく
    x=ab[i][0]
    y=ab[i][1]
    adlist[x-1].append(y)
    adlist[y-1].append(x)

c=list(map(int,input().split()))

s=[list(map(int,input().split())) for _ in range(q)]
for i in range(q):
    if s[i][0]==1:
        now=s[i][1]-1
        print(c[now])
        for change in adlist[now]:
            c[change-1]=c[now]
    else:
        now=s[i][1]-1
        print(c[now])
        c[now]=s[i][2]


    

    