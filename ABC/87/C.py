n=int(input())
a=[]
for i in range(2):
    a.append(list(map(int,input().split())))

dp= [[-1 for i in range(n)] for j in range(2)]

dp[0][0]=a[0][0]
dp[1][0]=dp[0][0]+a[1][0]

for i in range(1,n):
    dp[0][i]=dp[0][i-1]+a[0][i]
    dp[1][i]=max(dp[1][i-1]+a[1][i],dp[0][i]+a[1][i])


#for i in range(2):
    #print(dp[i])
print(dp[-1][-1])