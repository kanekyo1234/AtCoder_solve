n,m=map(int,input().split())

lr=[list(map(int,input().split())) for _ in range(m)]
#print(lr)

imos=[0]*(n+1)
for i in lr:
    start,end=i
    imos[start-1]+=1
    imos[end]-=1


for i in range(1,n):
    imos[i]=imos[i-1]+imos[i]

print(imos.count(m))