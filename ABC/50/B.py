n=int(input())
t=list(map(int,input().split()))
m=int(input())
px=[list(map(int,input().split())) for _ in range(m)]

ans=sum(t)

for i in range(m):
    print(ans-t[px[i][0]-1]+px[i][1])


