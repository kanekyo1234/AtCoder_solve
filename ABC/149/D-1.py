n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=list(input())
if  n%k!=0:
    leng=n//k+1
else:
    leng=n//k
data=[[0 for i in range(leng)] for j in range(n//(n//k))]
ans=0
for i in range(0,n//(n//k)):
    for j in range(0,leng):
        if i+(k*j)>=n:
            break
        data[i][j]=t[i+(k*j)]
print(data)
rz=0
sz=1
pz=2
for j in range(0,n//(n//k)):
    dp=[[0 for x in range(3)] for y in range(leng)]
    if data[j][0]=='r':
        dp[0][rz]=0
        dp[0][sz]=0
        dp[0][pz]=p
    elif data[j][0]=='s':
        dp[0][rz]=r
        dp[0][sz]=0
        dp[0][pz]=0
    elif data[j][0]=='p':
        dp[0][rz]=0
        dp[0][sz]=s
        dp[0][pz]=0

    for i in range(1,leng):
        if data[j][i]=='r':
            dp[i][rz]=dp[i][rz]+max(dp[i-1][sz],dp[i-1][pz])
            dp[i][sz]=dp[i][sz]+max(dp[i-1][rz],dp[i-1][pz])
            dp[i][pz]=dp[i][pz]+p+max(dp[i-1][sz],dp[i-1][rz])
        elif data[j][i]=='s':
            dp[i][rz]=dp[i][rz]+r+max(dp[i-1][sz],dp[i-1][pz])
            dp[i][sz]=dp[i][sz]+max(dp[i-1][rz],dp[i-1][pz])
            dp[i][pz]=dp[i][pz]+max(dp[i-1][sz],dp[i-1][rz])
        elif data[j][i]=='p':
            dp[i][rz]=dp[i][rz]+max(dp[i-1][sz],dp[i-1][pz])
            dp[i][sz]=dp[i][sz]+s+max(dp[i-1][rz],dp[i-1][pz])
            dp[i][pz]=dp[i][pz]+max(dp[i-1][sz],dp[i-1][rz])
        else:
            dp[i][rz]=dp[i-1][rz]
            dp[i][sz]=dp[i-1][sz]
            dp[i][pz]=dp[i-1][pz]
    ans+=max(dp[-1][rz],dp[-1][sz],dp[-1][pz])
print(ans)
