n=int(input())
a=list(map(int,input().split()))
count=0
s=sum(a)
if n%2==0:
    for i in range(0,n,2):
        count+=a[i]
    s-=count
    print(max(s,count))

else:
    count1=0
    count2=0
    for i in range(n,3):
        count1+=a[i]
    for i in range(1,n,3):
        count2+=a[i]
    print(max(s-count1-count2,count1,count2))


