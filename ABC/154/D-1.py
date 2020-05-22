


n,k=map(int,input().split())
p=list(map(int,input().split()))

rui=[]
rui.append(p[0]/2+0.5)
for i in range(1,n):
    rui.append(rui[i-1]+(p[i]/2+0.5))

#print(rui)
ans=[]
ans.append(rui[k-1])
for i in range(n-k):
    ans.append(rui[k+i]-rui[i])
    #print(ans)
print(max(ans))