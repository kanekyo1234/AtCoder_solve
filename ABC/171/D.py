import collections
n=int(input())
a=list(map(int,input().split()))
q=int(input())
bc=[list(map(int,input().split())) for i in range(q)]
ac=collections.Counter(a)
#print(ac)
ans=sum(a)
for i in range(q):
    if ac[bc[i][0]]!=None:
        if ac[bc[i][1]]!=None:
            ans-=bc[i][0]*ac[bc[i][0]]
            ans+=bc[i][1]*ac[bc[i][0]]
            ac[bc[i][1]]+=ac[bc[i][0]]
            ac[bc[i][0]]=0
        else:
            ans-=bc[i][0]*ac[bc[i][0]]
            ans+=bc[i][1]*ac[bc[i][0]]
            ac[bc[i][1]] = ac[bc[i][0]]
            ac[bc[i][0]]=0

    print(ans)

