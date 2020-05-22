
n,k=map(int,input().split())
p=list(map(int,input().split()))
count=0
ans=[0]*(n-k+2)

for j in range(0,k):
    count+=(p[j]/2+0.5)
ans[0]=count
z=1
#print(ans)
for i in range(k,n):
    #print(p[i],p[z-1])
    ans[z]=ans[z-1]-(p[z-1]/2+0.5)+(p[i]/2+0.5)
    z+=1
#print(ans)
print(max(ans))
"""
n,k=map(int,input().split())
p=list(map(int,input().split()))
count=0
ans=[]
for i in range(n-k+1):
    for j in range(i,k+i):
        count+=(p[j]/2+0.5)

    ans.append(count)
    count=0
print(ans)
print(max(ans))
"""