import collections
n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]
x=[]
y=[]
for i in range(n):
    for j in range(n):
        x.append(xy[i][0]-xy[j][0])
        y.append(xy[i][1]-xy[j][1])
ax=collections.Counter(x)
ay=collections.Counter(y)
print(n-max(ax.most_common()[0][1],ay.most_common()[0][1]))