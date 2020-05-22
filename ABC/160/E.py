x,y,a,b,c=map(int,input().split())
p=list(map(int,input().split()))#aこ
q=list(map(int,input().split()))#bko
r=list(map(int,input().split()))#cko
ans=0
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
ac=x-1
bc=y-1
for i in range(c):
    #print("DFGH")
    if p[ac]<q[bc] and p[ac]<r[i]:
        p[ac]=r[i]
        ac=max(0,ac-1)
    
    elif p[ac] >= q[bc] and q[bc]<r[i]:
        q[bc]=r[i]
        bc=max(0,bc-1)
for i in range(x):
    ans+=p[i]    
for i in range(y):
    ans+=q[i]
print(ans)
