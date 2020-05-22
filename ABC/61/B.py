n,m=map(int,input().split())
a=[]
for i in range(m):
    b,c=map(int,input().split())
    a.append(b)
    a.append(c)

for i in range(1,n+1):
    print(a.count(i))