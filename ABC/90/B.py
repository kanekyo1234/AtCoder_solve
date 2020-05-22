a,b=map(int,input().split())
ans=0
for i in range(a,b+1):
    d=list(str(i))
    dl=len(d)
    #print(dl)
    c=0
    for j in range(dl//2):
       # print(d[dl-1-i])
        if d[j]==d[dl-1-j]:
            c+=1
    if c==dl//2:
        ans+=1
print(ans)