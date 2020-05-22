n=int(input())
a=[]
v=list(map(int,input().split()))
c=list(map(int,input().split()))

for i in range(n):
    if v[i]-c[i]>0:
        a.append(v[i]-c[i])
print(sum(a))