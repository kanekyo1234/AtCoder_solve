n=int(input())
xy=[list(map(str,input().split())) for _ in range(n)]
ans=0
for i in range(n):
    if xy[i][1]=="BTC":
        ans+=380000*float(xy[i][0])
    else:
        ans+=float(xy[i][0])
print(ans)