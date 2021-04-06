n,m=map(int,input().split())

ab=[]
for i in range(m):
    ab.append(list(map(int,input().split())))

adlist_ab=[ [i+1] for i in range(n)]#交流のあるやつ同士の隣接リスト
for i in range(m):#1から順に見ていく
    x=ab[i][0]
    y=ab[i][1]
    adlist_ab[x-1].append(y)
    adlist_ab[y-1].append(x)
#print(adlist_ab)



def dfs(friends):
    chance=set()#友達＋候補
    for i in range(len(friends)):
        node=friends[i]-1
        for j in range(len(adlist_ab[node])):
            chance.add(adlist_ab[node][j])
    #print(chance)
    return n-(n-(max(0,len(chance)-len(friends))))

for i in range(n):
    friends=adlist_ab[i]
    #print(friends)
    #print(adlist)
    print(dfs(friends))#友達のところ

    """

for i in range(n):
    print(n-len(adlist_ab[i]))
"""