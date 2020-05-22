n=int(input())
b=list(map(int,input().split()))
ba=[]#右からの距離を足したやつ
for i in range(n):
    ba.append(b[i]+n-1-i)
print(ba)
ans=[]
ans.append(1)
for i in range(n-1,-1,-1):
    for j in range(i,-1,-1):
        if len(ans)<b[i]:
            ans.append()


    