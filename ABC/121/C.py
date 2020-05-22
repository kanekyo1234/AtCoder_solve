n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort()

count=0

for i in range(n):
    if ab[i][1]>m:
        count+=ab[i][0]*m
        break
    else:
        count+=ab[i][0]*ab[i][1]
        m-=ab[i][1]

print(count)