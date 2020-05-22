n=int(input())
a=list(map(int,input().split()))
ma=max(a)
ma=ma//2
aaa=max(a)
ans=10**10
for i in range(n):
    if abs(ma-a[i])<ans and a[i]!=aaa:
        ans=abs(ma-a[i])
        aaaaaa=a[i]
print(max(a),aaaaaa)

