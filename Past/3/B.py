n , m , q = map(int,input().split())
tokuten =[n]*m
seikai=[[] for _ in range(n)]

s=[list(map(int,input().split())) for _ in range(q)]
for i in range(q):
    if s[i][0]==1:
        ans=0
        for j in seikai[s[i][1]-1]:
            ans+=tokuten[j-1]
        print(ans)
    else:
        tokuten[s[i][2]-1]-=1
        seikai[s[i][1]-1].append(s[i][2])




        