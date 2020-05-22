n,m,k=map(int,input().split())

ab=[]
cd=[]
for i in range(m):
    ab.append(list(map(int,input().split())))

for i in range(k):
    cd.append(list(map(int,input().split())))


adlist_ab=[ [i+1] for i in range(n)]#交流のあるやつ同士の隣接リスト
for i in range(m):#1から順に見ていく
    x=ab[i][0]
    y=ab[i][1]
    adlist_ab[x-1].append(y)
    adlist_ab[y-1].append(x)
for i in range(k):#1から順に見ていく
    x=cd[i][0]
    y=cd[i][1]
    adlist_ab[x-1].append(y)
    adlist_ab[y-1].append(x)

for i in range(n):
    print(n-len(adlist_ab[i]),end=" ")