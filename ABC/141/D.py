n,m=map(int,input().split())

a=list(map(int,input().split()))


for i in range(m):
    a[a.index(max(a))]//=2
print(sum(a))
