n=int(input())
a=list(map(int,input().split()))
ans=0
if (sum(a)/n)%1!=0:
    print(-1)
    exit()
ave=sum(a)//n
count=0
for i in range(n):
    count+=a[i]-ave
    if count!=0:
        ans+=1
print(ans)
