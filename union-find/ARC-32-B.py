#多分union-find 
n,m=map(int,input().split())

ab=[list(map(int,input().split())) for _ in range(m)]

#adlist=[[i] for i in range(1,n+1)]
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

adlist=UnionFind(n+1)
#print(adlist.same(1,2))

for i in range(m):
    a=ab[i][0]
    b=ab[i][1]
    if adlist.same(a,b)==False:
        adlist.union(a,b)
print(adlist.group_count()-2)

"""
for i in range(m):
    x=ab[i][0]
    y=ab[i][1]
    adlist[x-1].append(y)
    adlist[y-1].append(x)
print(adlist)
for i in range()"""
