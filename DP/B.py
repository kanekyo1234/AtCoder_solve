# 2回目


n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [-1]*n

for i in range(min(k, n)):
    dp[i] = abs(h[i]-h[0])
# print(dp)

for i in range(k, n):
    # print(i)
    mindp = 10**9
    for j in range(i-k, i):
        # print(j)
        mindp = min(mindp, abs(h[i]-h[j])+dp[j])

    dp[i] = mindp
 #   print(dp[i])
# print(dp)
print(dp[-1])


"""

#1回目

n,x=map(int,input().split())
a=list(map(int,input().split()))
if n<=x:#ｎこのDPを作りたいのでｘが超えたらそれを変える必要がある
    x=n-1#でもこれは実際甘え

dp=[-1]*n

dp[0]=0#さいしょのところは０かかる
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
