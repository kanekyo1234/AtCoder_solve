n,l=map(int,input().split())
x1=list(map(int,input().split()))
t=list(map(int,input().split()))
x=[0]*(l+1)
for i in range(1,n):
    x[i]=x[i-1]
    if 
print(x)

"""
if n<=x:#ｎこのDPを作りたいのでｘが超えたらそれを変える必要がある
    x=n-1#でもこれは実際甘え

dp=[-1]*n

dp[0]=0#さいしょのところは０かかる
if x[1]==1:
    dp[1]=t[0]+t[2]
else:
    dp[1]=t[0]
dp[2]=min(dp[1]+t[0]+sum(x[]) , )
else:

for i in range(1,x+1):#飛べる距離までとべるところから最初の値を引く
    dp[i]=abs(a[i]-a[0])

for i in range(x+1,n):#さいしょのいちから飛べないところからDPを入れる
    min1=10**9
    for j in range(i-(x),i): # 最小を調べる繰り返し
        if min1>dp[j]+abs(a[j]-a[i]):               
            min1=dp[j]+abs(a[j]-a[i])#Xの数最小の値を調べる
    dp[i]=min1
print(dp[-1])
"""