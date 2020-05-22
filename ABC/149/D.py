n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=list(input())
if  n%k!=0:
    leng=n//k+1
else:
    leng=n//k
#上のif文がないと5 2 の時に[0,0][0,0]になってしまうので＋１する必要がある

data=[[0 for i in range(leng)] for j in range(k)]#7　3=[0,0,0][0,0,0][0,0,0] 5 4=[0,0,0,0][0,0,0,0]
ans=0
for i in range(0,k):
    for j in range(0,leng):
        if i+(k*j)<n:#来れないと配列を越しちゃう
            data[i][j]=t[i+(k*j)]
rz=0
sz=1
pz=2
#これらはDPのC問題と似たような感じでやっている
for j in range(0,k):
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
    #dpは最初に何を出すのか
    #dpはそこで繰り出して稼いだポイント＋それまでのポイントの値を示している
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