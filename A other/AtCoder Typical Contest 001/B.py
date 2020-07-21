class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):  # 要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  # 要素xが属するグループと要素yが属するグループとを併合する
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):  # 要素xが属するグループのサイズ（要素数）を返す
        return -self.parents[self.find(x)]

    def same(self, x, y):  # 要素x, yが同じグループに属するかどうかを返す

        return self.find(x) == self.find(y)

    def members(self, x):  # 要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):  # すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  # グループの数を返す
        return len(self.roots())

    def all_group_members(self):  # all_group_members O(N)かかるので注意
        return {r: self.members(r) for r in self.roots()}


n, q = map(int, input().split())
p, a, b = [], [], []
uf = UnionFind(n+1)

for i in range(q):
    s, d, f = map(int, input().split())
    p.append(s)
    a.append(d)
    b.append(f)

for i in range(q):
    if p[i] == 0:
        if uf.same(a[i], b[i]) == False:
            uf.union(a[i], b[i])
    else:
        if uf.same(a[i], b[i]):
            print("Yes")
        else:
            print("No")
