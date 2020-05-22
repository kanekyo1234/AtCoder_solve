n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
#print(a)
ad=sum(a)
#print(ad)
ad=ad/(4*m)
#print(ad)

for i in range(m):
    if a[i]<ad:
        print("No")
        break
else:
    print("Yes")
