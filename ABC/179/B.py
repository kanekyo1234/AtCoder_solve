n=int(input())
ans=0
count=0
for i in range(n):
    a,b=map(int,input().split())
    if a==b:
        count+=1
    else:
        ans=max(ans,count)
        count=0
ans=max(ans,count)
if ans>=3:
    print("Yes")
else:
    print("No")