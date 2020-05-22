n,c,k=map(int,input().split())
a=[int(input()) for _ in range(n)]

a.sort()
count=0
c_count=1
box=a[0]
for i in range(1,n):
    if c_count<c:
        if a[i]-box<=k:
            count+=1
            c_count+=1
        else:
            box=a[i]
            c_count=1
    else:
        box=a[i]
        c_count=1
    #print(count)
print(n-count)
