n,a,b=map(int,input().split())
ans=0
for i in range(1,n+1):
    im=i
    count=[]
    for j in range(37):
        count.append(i%10)
        i=i//10
    csum=sum(count)
    if a<=csum and csum<=b:
        #print(csum)
        ans+=im
print(ans)