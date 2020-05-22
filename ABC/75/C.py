n,m=map(int,input().split())
ab=[]
for i in range(m):
    ab.append(list(map(int,input().split())))

ans=0
def dfs(start,finish):
    global ans
    finish.add(start)#もう訪れたところ
   # print(finish)
    if len(finish)==n:#全部回ってたら終了
        ans+=1#橋じゃない数
        return 
    for i in adlist[start-1]:

        if i not in finish:#通ったところに入っていないなら通れるということ   
            dfs(i,finish)

for i in range(m):
    adlist=[]
    for h in range(n):    
        adlist.append([])
    for j in range(m):
        if i!=j:
            x=ab[j][0]
            y=ab[j][1]
            adlist[x-1].append(y)
            adlist[y-1].append(x)
    finish=set()
    #print(adlist)
    dfs(1,finish)#引数がけすノード
    
#print(adlist)

print(m-ans)

"""
iのノードを消したときすべてのところを回れるかというう動作をn回繰り返す
こればつ
ノードを消していたから違う線を消さなければならない
だからそれぞれのはしがないと金の隣接リストを作らないイケナイ
"""