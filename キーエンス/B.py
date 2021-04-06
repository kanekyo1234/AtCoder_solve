n=int(input())
x=[]
l=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append(a)
    l.append(b)

ans = [[0 for i in range(2)] for j in range(n)]
for i in range(n):
    ans[i][1]=(x[i]+l[i])
    ans[i][0]=max(0,x[i]-l[i])
ans.sort()
count=1
j=0
for i in range(n-1):
    
    if ans[j][1]<=ans[i+1][0] :
        count+=1
        j=i+1
    else:
        if ans[j][1]>ans[i+1][1]:
           j=i+1  
print(count)

