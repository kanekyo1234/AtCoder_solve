n,k=map(int,input().split())

x=list(map(int,input().split()))
ans=[]
for i in range(n-k+1):
    ans.append(min(abs(x[i])+x[i+k-1]-x[i] , abs(x[i+k-1])+(x[i+k-1]-x[i])))
    
print(min(ans))