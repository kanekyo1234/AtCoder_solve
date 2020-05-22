n,q=map(int,input().split())

imos=[0]*(n+1)

lr=[list(map(int,input().split())) for _ in range(q) ]

for i in range(q):
    imos[lr[i][0]-1]+=1
    imos[lr[i][1]]-=1
   # print(imos)

for i in range(1,n):
    imos[i]+=imos[i-1]

for i in range(n):
    print(imos[i]%2,end="")
print()

