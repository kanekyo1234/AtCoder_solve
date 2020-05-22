n=int(input())

a=list(map(int,input().split()))
b=[0]*n
cen=n//2
if n%2:#n%2==1
    for i in range(0,n):
        if i%2==1:
            b[cen+(i+1)//2]=a[i]
        else:
            b[cen-(i+1)//2]=a[i]
else:
    for i in range(0,n):
        if i%2==1:
            b[cen-(i+1)//2]=a[i]
        else:
            b[cen+(i+1)//2]=a[i]
"""
for i in range(n):
    b.append(a[i])
    b.reverse()
"""
for i in range(n):
    print(b[i],end=" ")