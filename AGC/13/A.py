n=int(input())
a=list(map(int,input().split()))
ans=1
now=a[0]
start=1

if n==1:
    print(1)
    exit()

while now==a[start]:
    start+=1
if a[0]<a[start]:#増加
    jugh=1
else:#現象
    jugh=2
#print(start,jugh)
i=start
while i<n:
    if jugh==0:
        while now==a[start]:
            start+=1
        if now<a[start]:#増加
            jugh=1
        else:#現象
            jugh=2
            
    if jugh==1:
        if a[i-1]>a[i]:
            jugh=0
            ans+=1
            now=a[i]
            start=i+1
            #print(a[i-1],a[i])
                
    else:
        if a[i-1]<a[i]:
            jugh=0
            ans+=1
            now=a[i]
            start=i+1
            #print(a[i-1],a[i])
            
    i+=1   

print(ans)