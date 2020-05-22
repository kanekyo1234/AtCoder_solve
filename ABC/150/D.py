n,m=map(int,input().split())

a=list(map(int,input().split()))

a=list(set(a))
m*=len(a)
sa=1
p=0
for i in range(len(a)):
    m=m/a[i]
if m<1:
    print("0")
else:
    print(int(m)+1)
