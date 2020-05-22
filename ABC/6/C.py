n,m=map(int,input().split())
limit=10**5
if m%2==1:
    old = 1
    m-=3
    n-=1
else:
    old = 0
#print(n,m)
grown = (4*n-m)//2 #大人２ 2
child = (n-grown)

if min(grown,old,child)<0 or grown*2+child*4!=m :
    print(-1,-1,-1)
else:
    print(grown,old,child)