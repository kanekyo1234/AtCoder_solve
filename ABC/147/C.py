"""n=int(input())
c=[[0] * n for i in range(n)]
for i in range(n):
    a=int(input())
    e=[[int(i) for i in input().split()] for i in range(a)] 
    for j in range(b):
        c[i][e[j][0]-1]=e[j][1]
print(c)
"""
import copy
n=int(input())
xy=[[] for i in range(n)]

for i in range(n):
    a=int(input())
    for j in range(a):
        xy[i].append(list(map(int, input().split())))
xyc=copy.deepcopy(xy)

print(xy)
for i in range(2**n):
    bit=[0]*n
    for j in range(n):
        if ((i >> j) & 1):
            bit[j]=1
    print(bit)#0が嘘つき1が正直
    for j in range(n):
        for z in range(len(xy[j])):
            if bit[j]==0:
                if xy[j][z][1]==1:
                    xy[j][z][1]=0
                else:
                    xy[j][z][1]=1
    
    print(xy)
    print(xyc)
    xy=copy.deepcopy(xyc)
print(xy)

"""

再起で
def dfs():
if len(bit)==n:
    ここで正しいか正しくないかの判定でcountする
else:
    dfs(bit+[0]
    dfe(bit+[1]

このやり方だと関数にbitを持っていきやすい
最初にbitを全部作るのではなく楽にb書くことができる。


"""