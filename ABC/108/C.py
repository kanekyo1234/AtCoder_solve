n,k=map(int,input().split())

if k%2==1:
    print((n//k)**3)
    exit()
ans=0
#全部偶数か全部奇数

#偶数k%2==0
ans+=((n//k)**3)
#奇数and 余りが０、k/2
count=0
for i in range(1,n+1):
    if i%k==k//2:
        count+=1
ans+=count**3

print(ans)

