n,m=map(int,input().split())

ab=[list(map(int,input().split())) for _ in range(m)]

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):#要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):#要素xが属するグループと要素yが属するグループとを併合する
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):#要素xが属するグループのサイズ（要素数）を返す
        return -self.parents[self.find(x)]

    def same(self, x, y):#要素x, yが同じグループに属するかどうかを返す

        return self.find(x) == self.find(y)

    def members(self, x):#要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):#すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):#グループの数を返す
        return len(self.roots())

    def all_group_members(self):#all_group_members O(N)かかるので注意
        return {r: self.members(r) for r in self.roots()}

uf=UnionFind(n+1)

for i in range(m):
    a=ab[i][0]
    b=ab[i][1]
    if uf.same(a,b)==False:
        uf.union(a,b)

#print(uf.all_group_members())
#print(uf.size(2))
if uf.group_count()!=2:
    print("NO")
    exit()
print("Yes")
ans=[0]*n
for i in range(m):
    if ans[ab[i][0]-1]==0:
        ans[ab[i][0]-1]=ab[i][1]
    if ans[ab[i][1]-1]==0:
        ans[ab[i][1]-1]=ab[i][0]

for i in range(1,n):
    print(ans[i])














"""
def dijkstra(s,n,w,cost):
    #始点sから各頂点への最短距離
    #n:頂点数,　w:辺の数, cost[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    
    while True:
        v = -1
        #まだ使われてない頂点の中から最小の距離のものを探す
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True
               
        for j in range(n):
               d[j] = min(d[j],d[v]+cost[v][j])
    return d

################################
#print(ab[0])
cost = [[float("inf") for i in range(n)] for i in range(n)] 
#cost[u][v] : 辺uvのコスト(存在しないときはinf この場合は10**10)
for i in range(m):
    x,y,z = ab[i]
    cost[x-1][y-1] = z
    cost[y-1][x-1] = z
ans=dijkstra(0,n,m,cost)
#print(ans)
print("Yes")
for i in range(1,n):
    print(ans[i])

"""
