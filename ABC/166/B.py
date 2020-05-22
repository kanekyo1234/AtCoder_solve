n,k=map(int,input().split())
a=[0]*n
for i in range(k):
    d=int(input())
    a1=list(map(int,input().split()))
    for j in range(d):
        a[a1[j]-1]+=1

print(a.count(0))
