
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=-1
count=0
min=111111111111111
for i in range(0,n,1):
    count+=a[i]
    if count>=b[i]:
        if min>b[i]:
            min=b[i]
            ans=min
print (ans)






