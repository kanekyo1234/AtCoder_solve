n,m=map(int,input().split())
a=list(map(int,input().split()))
bc=[list(map(int,input().split())) for _ in range(m)]


bc=sorted(bc, key=lambda x:(x[1], x[0]), reverse=True)
count=0
i=0
while count<n and i<m:
    for j in range(bc[i][0]):
        a.append(bc[i][1])
        count+=1
    i+=1
    

a.sort(reverse=True)
#print(a)
ans=0
for i in range(n):
    ans+=a[i]
print(ans)