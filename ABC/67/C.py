n=int(input())
a=list(map(int,input().split()))

x=[a[0]]

for i in range(1,n-1):
    x.append(x[i-1]+a[i])
y=[sum(a)-a[0]]
for i in range(1,n-1):
    y.append(y[i-1]-a[i])
#print(x)
#print(y)

ans=10**100
for i in range(n-1):
    ans=min(ans,abs(x[i]-y[i]))
print(ans)

"""    
for i in range(2,n):
    if a[i]<0:
        if x>y:
            x+=a[i]
        else:
            y+=a[i]
    else:
        if x<y:
            x+=a[i]
        else:
            y+=a[i]
print(max(x,y)-min(x,y))"""