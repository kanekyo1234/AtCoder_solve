n=int(input())
a=list(map(int,input().split()))

ans=[0]*8
count=0
for i in range(n):
    if 8<=a[i]//400:
        count+=1
    else:
        ans[a[i]//400]=1
#print(ans)
if sum(ans)==0:
    print(1,min(8,count))
else:
    print(sum(ans),sum(ans)+count)

