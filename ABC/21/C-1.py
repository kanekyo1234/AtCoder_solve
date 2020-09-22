n=int(input())
a,b=map(int,input().split())
m=int(input())

xy=[list(map(int,input().split())) for _ in range(m)]

adlist=[[i] for i in range(1,n+1)]

for i in xy:
    x,y=i
    adlist[x-1].append(y)
    adlist[y-1].append(x)
print(adlist)

