n,x,m=map(int,input().split())

a=list(map(int,input().split()))
ans1=0
ans2=0
for i in range(m,n+1):
    print(i)
    if i in a:
        ans1+=1
for i in range(0,m+1):
    if i in a:
        ans2+=1
print(ans1,ans2)
print(min(ans1,ans2))
