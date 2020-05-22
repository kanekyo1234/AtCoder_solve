n=int(input())
a=list(int(input()) for i in range(n))
max1=sum(a)
a.sort()
count=0
for i in range(n):
    if max1%10==0:
        if a[i]%10!=0:
           max1-=a[i]
        else:
           count+=1
if count==n:
    print(0)
else:
    print(max1)
