w,h,n=map(int,input().split())
x=[]
y=[]
a=[]
for i in range(n):
    a1,b,c=map(int,input().split())
    x.append(a1)
    y.append(b)
    a.append(c)

w1=0#左の削り
w2=0#右の削り
h1=0#下の削り
h2=0#上の削り
for i in range(n):
    if a[i]==1:
        w1=max(w1,x[i])
    if a[i]==2:
        w2=max(w2,w-x[i])
    if a[i]==3:
        h1=max(h1,y[i])
    if a[i]==4:
        h2=max(h2,h-y[i])


if (w-w1-w2)<0 and (h-h1-h2)<0:
    print(0)
else:
    print(max(0,(w-w1-w2)*(h-h1-h2)))


