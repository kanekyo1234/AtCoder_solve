n,m=map(int,input().split())
x=list(map(int,input().split()))
if n>=m:
    print("0")
    exit()
x.sort()
a=[0]
for i in range(m-1):
   a.append(x[i+1]-x[i])
a.sort(reverse=True)
for i in range(n-1):
    a[i]=0
print(sum(a))