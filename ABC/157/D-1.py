
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
    
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
 

n,m,k=map(int,input().split())

uf=UnionFind(n+1)
ab=[]
cd=[]
for i in range(m):
    ab.append(list(map(int,input().split())))

for i in range(k):
    cd.append(list(map(int,input().split())))
#入力

for i in range(m):
   # print("gn")
    a=ab[i][0]
    b=ab[i][1]
    if uf.same(a,b)==False:
        uf.union(a,b)


friend=[]
for i in range(1,n+1):
    friend.append(uf.size(i))
print(friend)

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
    print(len(adlist_ab[i]),end=" ")
print()

for i in range(n):
    print(friend[i]-len(adlist_ab[i]),end=" ")