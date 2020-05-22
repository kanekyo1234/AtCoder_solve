h,n=map(int,input().split())
dp = [[0 for i in range(h+1)] for j in range(n+1)]
a=[]
b=[]
for i in range(n):
    k,l=map(int,input().split())
    a.append(k)
    b.append(l)
print(dp)

for i in range(h):     
    for j in range(n):
        dp[i][j]=min(dp[])
    i+=1
print(dp)