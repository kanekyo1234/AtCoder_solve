n,m=map(int,input().split())
xy = [ list(map(int,input().split())) for _ in range(m) ]

ans=0
jagh=[0]*n#あかがはいった事あるかどうか
jagh[0]=1
now=[1]*n#ボールの個数
for i in range(m):
    if jagh[xy[i][0]-1]==1:
        jagh[xy[i][1]-1]=1
        now[xy[i][0]-1]-=1
        if now[xy[i][0]-1]==0:
            jagh[xy[i][0]-1]=0
        now[xy[i][1]-1]+=1
    else:
        now[xy[i][0]-1]-=1
        if now[xy[i][0]-1]==0:
            jagh[xy[i][0]-1]=0
        now[xy[i][1]-1]+=1

#print(jagh,now)
for i in range(n):
    if jagh[i]==1 and 0<now[i]:
        ans+=1
print(ans)